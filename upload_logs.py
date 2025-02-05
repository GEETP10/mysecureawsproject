import boto3

# Define AWS S3 Bucket
BUCKET_NAME = "mysecureprojectg"

# Initialize S3 Client
s3 = boto3.client("s3")

# Upload a file
file_name = "security_logs.txt"
s3.upload_file(file_name, BUCKET_NAME, file_name)

print(f"Uploaded {file_name} to S3 bucket {BUCKET_NAME}")