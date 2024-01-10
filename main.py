import pyautogui
import random
import time

# The boundaries of the dirt plot in your game
# Update these values according to your screen and game
left, top, width, height = 100, 100, 800, 600

def get_random_location_within_bounds():
    x = random.randint(left, left + width)
    y = random.randint(top, top + height)
    return x, y

def automate_game():
    while True:
        x, y = get_random_location_within_bounds()
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        time.sleep(2)  # Wait for the character to move
        pyautogui.press('d')
        time.sleep(15)  # Wait 15 seconds before repeating

if __name__ == "__main__":
    automate_game()

