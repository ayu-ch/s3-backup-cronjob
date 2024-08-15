FROM python:alpine

COPY backup.py /
COPY /data /data/
COPY entrypoint.sh /
COPY .env /
RUN pip install boto3 awscli python-dotenv

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/bin/sh","/entrypoint.sh"]
