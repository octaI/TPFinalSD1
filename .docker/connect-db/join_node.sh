#!/usr/bin/env bash

DBCENTER=$1

sed -e "s/EXTERN_NODE/${DBCENTER}/" template.yml > docker-compose.yml

docker-compose up