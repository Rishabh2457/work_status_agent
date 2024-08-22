# workstatus_agent/screenshot_manager.py
from PIL import ImageGrab, ImageFilter
import time
import os

class ScreenshotManager:
    def __init__(self, config):
        self.blur = config.get('blur', False)
        self.screenshot_interval = config.get('screenshot_interval', 10)
        self.screenshot_path = config.get('screenshot_path', './screenshots')

    def capture_screenshot(self):
        screenshot = ImageGrab.grab()
        if self.blur:
            screenshot = screenshot.filter(ImageFilter.GaussianBlur(15))
        if not os.path.exists(self.screenshot_path):
            os.makedirs(self.screenshot_path)
        screenshot_file = os.path.join(self.screenshot_path, f"screenshot_{int(time.time())}.png")
        screenshot.save(screenshot_file)
        return screenshot_file

    def start_screenshot_loop(self):
        while True:
            self.capture_screenshot()
            time.sleep(self.screenshot_interval)
