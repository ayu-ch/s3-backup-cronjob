#!/bin/sh

echo -e "* * * * * python /backup.py" >> /etc/crontabs/root

crond -f