import boto3
import os
import time
from dotenv import load_dotenv

load_dotenv()

s3_resource = boto3.resource(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

bucket_name = os.getenv('BUCKET_NAME')
bucket = s3_resource.Bucket(name=bucket_name)

backups = list(bucket.objects.filter(Prefix='backup/'))

latest_backup = max(backups, key=lambda obj: obj.last_modified)  

backup_file_remote = latest_backup.key
local_dir = '/data/backup'
backup_file_local = os.path.join(local_dir, os.path.basename(backup_file_remote))

os.makedirs(local_dir, exist_ok=True)

bucket.download_file(backup_file_remote, backup_file_local)

print(f"Backup file '{backup_file_local}' downloaded successfully.")
