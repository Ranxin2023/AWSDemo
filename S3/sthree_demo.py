import boto3
from dotenv import load_dotenv
import os
load_dotenv()
s3 = boto3.client('s3')

bucket_name = os.getenv("bucketName")     # Replace with your bucket name
file_path = 's3_demo_file.txt'              # File on your machine
object_name = 'uploaded_file.txt'         # Name for the file in S3

s3.upload_file(file_path, bucket_name, object_name)

print(f"Uploaded {file_path} to S3 bucket {bucket_name} as {object_name}")
