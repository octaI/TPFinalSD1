#!/usr/bin/env bash

/cockroach/cockroach.sh start --insecure &\
echo 'Waiting to init';sleep 15; /cockroach/cockroach.sh  user set distribuidos --insecure &&\
/cockroach/cockroach.sh sql --insecure -e 'CREATE DATABASE IF NOT EXISTS Election' &&\
/cockroach/cockroach.sh sql --insecure -e 'GRANT ALL ON DATABASE Election TO distribuidos'

tail -f /dev/null