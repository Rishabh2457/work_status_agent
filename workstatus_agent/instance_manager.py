# workstatus_agent/instance_manager.py
import os
import sys

class InstanceManager:
    @staticmethod
    def check_instance():
        lock_file = 'agent.lock'
        if os.path.exists(lock_file):
            print("Instance already running.")
            sys.exit()
        else:
            open(lock_file, 'w').close()

    @staticmethod
    def release_instance():
        os.remove('agent.lock')
