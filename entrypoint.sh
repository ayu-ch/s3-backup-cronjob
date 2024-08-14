#!/bin/sh

echo -e "0 0 * * * python backup.py" >> /etc/crontabs/root

crond -f