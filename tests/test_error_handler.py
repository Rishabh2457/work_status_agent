import logging
logging.disable(logging.CRITICAL)  # This suppresses all log messages at CRITICAL level and below

# tests/test_error_handler.py
import unittest
from workstatus_agent.error_handler import ErrorHandler

class TestErrorHandler(unittest.TestCase):
    def test_handle_no_internet(self):
        self.assertIsNone(ErrorHandler.handle_no_internet())  # Check that the method returns None

if __name__ == '__main__':
    unittest.main()
