#!/bin/bash

echo Wait for servers to be up
sleep 5

HOSTPARAMS="--host roach-1 --insecure"
SQL="/cockroach/cockroach.sh sql $HOSTPARAMS"

$SQL < /devel/db/v1/v1.sql