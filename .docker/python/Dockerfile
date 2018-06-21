FROM python:3

WORKDIR /devel/

COPY requirements.txt /
COPY .docker/python/startup.sh /

RUN ["pip","install","--no-cache-dir","-r","/requirements.txt"]t