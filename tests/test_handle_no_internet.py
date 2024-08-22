import unittest
import logging
from workstatus_agent.error_handler import ErrorHandler

class TestErrorHandler(unittest.TestCase):
    def test_handle_no_internet(self):
        with self.assertLogs('root', level='CRITICAL'):
            ErrorHandler.handle_no_internet()
        # Alternatively, suppress logging globally for this test
        # logging.disable(logging.CRITICAL)
        # ErrorHandler.handle_no_internet()
        # logging.disable(logging.NOTSET)

if __name__ == '__main__':
    unittest.main()
