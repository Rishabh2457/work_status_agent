import unittest
from workstatus_agent.activity_tracker import ActivityTracker

class TestActivityTracker(unittest.TestCase):
    def test_activity_detection(self):
        tracker = ActivityTracker()
        self.assertIsNotNone(tracker.detect_activity)

if __name__ == '__main__':
    unittest.main()