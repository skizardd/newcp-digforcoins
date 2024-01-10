from pynput.mouse import Listener
import logging

# Set up logging to record the coordinates of clicks
logging.basicConfig(filename="mouse_clicks.log", level=logging.INFO, format='%(asctime)s: %(message)s')

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

# Set up the listener
with Listener(on_click=on_click) as listener:
    listener.join()
