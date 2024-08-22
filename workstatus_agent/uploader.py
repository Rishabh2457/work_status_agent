# workstatus_agent/uploader.py
import boto3
import os
import logging

class S3Uploader:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key):
        self.s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        self.bucket_name = bucket_name

    def upload_file(self, file_name):
        try:
            self.s3.upload_file(file_name, self.bucket_name, os.path.basename(file_name))
            os.remove(file_name)
            print(f"Uploaded and deleted {file_name}.")
        except Exception as e:
            logging.error(f"Failed to upload {file_name}: {str(e)}")

    def upload_files_in_directory(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                self.upload_file(os.path.join(root, file))
