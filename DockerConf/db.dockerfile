FROM postgres:9.6

MAINTAINER wimness@163.com

RUN rm /etc/apt/sources.list
COPY DockerConf/sources.list /etc/apt/sources.list
# RUN apt-get update