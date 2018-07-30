#!/usr/bin/env bash

pip install --no-cache-dir -r /devel/requirements.txt

export PYTHONPATH=/devel

cd /devel/app

mkdir -p ../log
LOGFILE=../log/error.log

gunicorn main:app -w 9  --keep-alive 300 --access-logfile ../log/access.log --error-logfile ${LOGFILE} --log-file ${LOGFILE} --log-level debug --reload -b 0.0.0.0:8080