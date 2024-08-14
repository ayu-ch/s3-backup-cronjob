import boto3
import os
import tarfile
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

timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

backup_fileout_name = f'backup-{timestamp}.tar.gz'

out_tar_local = f'/tmp/{backup_fileout_name}'

with tarfile.open(out_tar_local, 'w:gz') as tar:
    tar.add('/data', recursive=True)

out_tar_remote = f'backup/{backup_fileout_name}'

bucket.upload_file(out_tar_local, out_tar_remote)

os.remove(out_tar_local)

