# tests/test_timezone_manager.py
import unittest
from workstatus_agent.timezone_manager import TimezoneManager

class TestTimezoneManager(unittest.TestCase):
    def test_timezone_detection(self):
        tz_manager = TimezoneManager()
        self.assertIsNotNone(tz_manager.current_timezone)

if __name__ == '__main__':
    unittest.main()
