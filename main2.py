import pyautogui
import random
import time
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

def get_random_location_within_bounds(poly):
    while True:
        x = random.randint(min(x for x, y in poly), max(x for x, y in poly))
        y = random.randint(min(y for x, y in poly), max(y for x, y in poly))
        if is_point_in_poly(x, y, poly):
            return x, y

def automate_game(poly):
    while True:
        x, y = get_random_location_within_bounds(poly)
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        time.sleep(3)  # Wait for the character to move
        pyautogui.press('d')
        time.sleep(15)  # Wait 15 seconds before repeating

if __name__ == "__main__":
    automate_game(polygon_coords)
