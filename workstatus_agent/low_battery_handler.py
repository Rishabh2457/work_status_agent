# workstatus_agent/low_battery_handler.py
import psutil

class LowBatteryHandler:
    def __init__(self):
        self.low_battery_threshold = 20  # percent

    def monitor_battery(self):
        battery = psutil.sensors_battery()
        if battery.percent < self.low_battery_threshold and not battery.power_plugged:
            print("Low battery detected. Suspending activity tracking.")
            return False  # Suspend activity
        return True  # Continue activity
