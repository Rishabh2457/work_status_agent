# workstatus_agent/timezone_manager.py
import time

class TimezoneManager:
    def __init__(self):
        self.current_timezone = time.tzname

    def detect_timezone_change(self):
        while True:
            if time.tzname != self.current_timezone:
                self.current_timezone = time.tzname
                print(f"Timezone changed to {self.current_timezone}.")
            time.sleep(60)
