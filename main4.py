import pyautogui
import cv2
import numpy as np
import random
import time
from datetime import datetime
from matplotlib.path import Path

# Define the vertices of the polygon (dirt plot) with your provided coordinates
polygon_coords = [
    (758, 799),
    (1105, 835),
    (1167, 798),
    (1356, 794),
    (1336, 713),
    (1157, 682),
    (1122, 706),
    (962, 631),
    (845, 615),
    (714, 672),
    (632, 750)
]

def is_point_in_poly(x, y, poly):
    path = Path(poly)
    return path.contains_point((x, y))

def get_random_location_within_bounds(poly, last_point=None):
    while True:
        x = random.randint(min(x for x, y in poly), max(x for x, y in poly))
        y = random.randint(min(y for x, y in poly), max(y for x, y in poly))
        current_point = (x, y)
        if is_point_in_poly(x, y, poly) and current_point != last_point:
            return current_point

def check_for_popup_and_close(reference_image_path, tolerance=0.8):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # Load the reference image (the "X" button)
    reference_image = cv2.imread(reference_image_path, 0)
    w, h = reference_image.shape[::-1]

    # Convert screenshot to grayscale
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Match the reference image in the screenshot
    res = cv2.matchTemplate(gray_screenshot, reference_image, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= tolerance)

    # If found, click the "X" button
    for pt in zip(*loc[::-1]):
        pyautogui.click(pt[0] + w/2, pt[1] + h/2)
        return True
    return False

def automate_game(poly, popup_image_path):
    start_time = datetime.now()
    print("Script started at:", start_time.strftime("%Y-%m-%d %H:%M:%S"))

    last_point = None
    try:
        while True:
            if check_for_popup_and_close(popup_image_path):
                print("Popup closed, returning to the game")
                time.sleep(2)  # Brief pause after closing the popup

            x, y = get_random_location_within_bounds(poly, last_point)
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            last_point = (x, y)  # Update the last point
            time.sleep(3)  # Wait for the character to move
            pyautogui.press('d')
            time.sleep(15)  # Wait 15 seconds before repeating

    except KeyboardInterrupt:
        stop_time = datetime.now()
        print("Script stopped at:", stop_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Total run time:", stop_time - start_time)

if __name__ == "__main__":
    popup_image_path = 'C:\\Users\\skiz\\OneDrive\\Desktop\\My Stuff\\newcp-x-button-grayscale.png'
    automate_game(polygon_coords, popup_image_path)
