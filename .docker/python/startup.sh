#!/usr/bin/env bash

pip install --no-cache-dir -r /devel/requirements.txt

export PYTHONPATH=/devel

python /devel/app/main.py