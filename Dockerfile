FROM ubuntu:20.04

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
COPY . /code/

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y build-essential
RUN apt-get install -y libssl-dev
RUN apt-get install -y python-dev
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pwd
RUN ls
RUN pip install -r requirements.txt

