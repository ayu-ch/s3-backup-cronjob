FROM python:3.8-alpine

COPY backup.py /
COPY /folder /backup/
COPY entrypoint.sh /

RUN pip install boto3 awscli

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/bin/sh","/entrypoint.sh"]
