import pyautogui
import pydirectinput


def process_key(message):
    keys = ["up", "down", "left", "right", "a", "b", "start", "select"]
    if message in keys:
        return message
    else:
        return "invalid"


def press_key(message):
    key_mappings = {
        "up": "w",
        "down": "s",
        "left": "a",
        "right": "d",
        "a": "z",
        "b": "x",
        "start": "o",
        "select": "p"
    }
    pydirectinput.press(key_mappings[message])
    print("Pressed " + key_mappings[message])
