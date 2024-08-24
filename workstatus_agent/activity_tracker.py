import time
import pyautogui
import threading
import keyboard

class ActivityTracker:
    def __init__(self):
        self.last_mouse_position = pyautogui.position()

    def detect_keyboard(self):
        # Non-blocking check for keyboard events
        while True:
            event = keyboard.read_event()
            if event and event.event_type == keyboard.KEY_DOWN:
                print(f"User activity detected (key press): {event.name}")

            # Break out of the loop gracefully with ESC key
            if keyboard.is_pressed('esc'):
                print("Exiting activity tracker.")
                exit()

    def detect_activity(self):
        while True:
            # Continuously check if the mouse position has changed
            current_mouse_position = pyautogui.position()
            if current_mouse_position != self.last_mouse_position:
                self.last_mouse_position = current_mouse_position
                print("User activity detected (mouse movement).")

            if keyboard.is_pressed('esc'):
                print("Exiting activity tracker.")
                exit()
                
            # Small delay to reduce CPU usage
            time.sleep(0.05)

    def start(self):
        print("Starting activity tracker. Press 'ESC' to exit.")
        activity_thread = threading.Thread(target=self.detect_activity)
        keyboard_thread = threading.Thread(target=self.detect_keyboard)

        # Start the threads
        activity_thread.start()
        keyboard_thread.start()

        # Wait for both threads to finish (mainly for graceful exit)
        activity_thread.join()
        keyboard_thread.join()

# Usage
tracker = ActivityTracker()
tracker.start()
