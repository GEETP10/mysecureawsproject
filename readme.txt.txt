🚀 AWS Security Project: Secure Log Storage & Monitoring

  Project Overview
This project implements a secure logging system on AWS, utilizing **Amazon S3 for storage**, **IAM roles for access control**, **AWS GuardDuty for threat detection**, and **AWS CloudWatch for monitoring**. Additionally, the project includes **Python automation** for log uploads and is fully documented in GitHub.

 🛠 Technologies & AWS Services Used
- **Amazon S3** – Secure storage for logs.
- **IAM (Identity & Access Management)** – Access control for S3.
- **AWS CLI** – Command-line tool to interact with AWS.
- **AWS GuardDuty** – Security threat detection.
- **AWS CloudWatch** – Monitoring and alerting system.
- **Python (Boto3 SDK)** – Automating file uploads.
- **GitHub** – Documentation and version control.

 📂 Project Structure

 🚀 Steps to Run the Project

 1️⃣ **Setup AWS CLI**
step 1. Configure AWS CLI with IAM credentials
 command:  "aws configure"
2️⃣ Create an S3 Bucket & Upload Logs
command "aws s3 ls"
command: "aws s3 mb s3://mysecureprojectg (creates s3 bucket)
command: "aws s3 cp security_logs.txt s3://mysecureprojectg/  (uploads the security log file to s3)
command: aws s3 ls s3://mysecureprojectg/ (verifies file in s3)
3️⃣ Set IAM Permissions
Assign IAM role with AmazonS3FullAccess for secure file access.
Restrict unnecessary permissions.
4️⃣ Enable GuardDuty for Security Monitoring
Enable GuardDuty in AWS Console
Enable S3 Protection
Monitor for security threats
5️⃣ Retrieve Logs from S3
Download logs from S3
command: aws s3 cp s3://mysecureprojectg/security_logs.txt .
View logs in the terminal
command:  type security_logs.txt #windows
          cat security_logs.txt #mac/Linux
6️⃣ Automate Log Uploads Using Python
Install dependencies
pip install boto3
Create upload_logs.py script
Run the Python script
python upload_logs.py
7️⃣ Setup CloudWatch Monitoring
Enable CloudWatch Metrics for S3 to monitor file uploads.
Configure CloudWatch Alarms for unusual activity.



