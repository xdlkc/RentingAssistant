FROM ubuntu
MAINTAINER wimness@163.com
RUN rm /etc/apt/sources.list
COPY DockerConf/source.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y python python-pip python-dev
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
COPY DockerConf/requirements.txt /code
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV PYTHONIOENCODING=utf-8



