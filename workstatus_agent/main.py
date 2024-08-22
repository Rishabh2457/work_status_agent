# workstatus_agent/main.py
import threading
from activity_tracker import ActivityTracker
from screenshot_manager import ScreenshotManager
from uploader import S3Uploader
from config_manager import ConfigManager
from timezone_manager import TimezoneManager
from error_handler import ErrorHandler
from instance_manager import InstanceManager

def main():
    InstanceManager.check_instance()
    
    try:
        config_manager = ConfigManager()
        config_manager.load_config()
        
        activity_tracker = ActivityTracker()
        screenshot_manager = ScreenshotManager(config_manager.config)
        uploader = S3Uploader(config_manager.config['bucket_name'], 
                              config_manager.config['aws_access_key'], 
                              config_manager.config['aws_secret_key'])
        timezone_manager = TimezoneManager()

        # Start threads
        threading.Thread(target=activity_tracker.start).start()
        threading.Thread(target=screenshot_manager.start_screenshot_loop).start()
        threading.Thread(target=timezone_manager.detect_timezone_change).start()
        threading.Thread(target=config_manager.listen_for_updates).start()

    except Exception as e:
        ErrorHandler.handle_abrupt_shutdown()
    finally:
        InstanceManager.release_instance()

if __name__ == "__main__":
    main()
