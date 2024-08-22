# workstatus_agent/security.py
import os
from cryptography.fernet import Fernet

class Security:
    def __init__(self):
        self.key = os.environ.get('ENCRYPTION_KEY', Fernet.generate_key())
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        return self.cipher_suite.encrypt(data)

    def decrypt_data(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data)
