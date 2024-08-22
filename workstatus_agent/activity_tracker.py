import time
import pyautogui
import keyboard

class ActivityTracker:
    def __init__(self):
        self.last_mouse_position = pyautogui.position()

    def detect_activity(self):
        while True:
            current_mouse_position = pyautogui.position()
            if current_mouse_position != self.last_mouse_position or keyboard.is_pressed('esc'):  # Example key
                self.last_mouse_position = current_mouse_position
                print("User activity detected.")
            else:
                print("No activity detected.")
            time.sleep(1)

    def start(self):
        self.detect_activity()
