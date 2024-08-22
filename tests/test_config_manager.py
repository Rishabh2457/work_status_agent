# tests/test_config_manager.py
import unittest
from workstatus_agent.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    def test_load_config(self):
        cm = ConfigManager('config.json')
        cm.load_config()
        self.assertIn('screenshot_interval', cm.config)

if __name__ == '__main__':
    unittest.main()
