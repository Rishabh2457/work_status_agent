import unittest
from tests.test_base import BaseTestCase  # Import BaseTestCase
from workstatus_agent.activity_tracker import ActivityTracker

class TestActivityTracker(BaseTestCase):  # Inherit from BaseTestCase
    def test_activity_detection(self):
        tracker = ActivityTracker()
        self.assertIsNotNone(tracker.detect_activity)

if __name__ == '__main__':
    unittest.main()
