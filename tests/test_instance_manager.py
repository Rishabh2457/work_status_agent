# tests/test_instance_manager.py
import unittest
from workstatus_agent.instance_manager import InstanceManager
import os

class TestInstanceManager(unittest.TestCase):
    def test_instance_check(self):
        InstanceManager.check_instance()
        self.assertTrue(os.path.exists('agent.lock'))
        InstanceManager.release_instance()
        self.assertFalse(os.path.exists('agent.lock'))

if __name__ == '__main__':
    unittest.main()
