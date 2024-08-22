# workstatus_agent/config_manager.py
import json
import os
import time

class ConfigManager:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as file:
            self.config = json.load(file)

    def apply_config(self):
        # Logic to apply configuration changes to relevant modules
        pass

    def listen_for_updates(self):
        last_modified = os.path.getmtime(self.config_path)
        while True:
            current_modified = os.path.getmtime(self.config_path)
            if current_modified != last_modified:
                self.load_config()
                self.apply_config()
                last_modified = current_modified
            time.sleep(5)
