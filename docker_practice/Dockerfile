FROM ubuntu 

ENV PYTHONBUFFER=1

RUN apt update -y
RUN apt upgrade -y
RUN apt install python3-pip curl -y
RUN pip install pipenv

RUN pipenv install pandas

