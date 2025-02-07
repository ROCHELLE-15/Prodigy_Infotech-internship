import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print(f'Pressed: {key.char}')
    except AttributeError:
        print(f'Pressed: {key}')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()