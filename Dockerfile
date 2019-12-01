FROM python:3.8-alpine

RUN mkdir /code

WORKDIR /code

RUN apk add --no-cache mariadb-dev build-base

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN chmod +x ./start.sh

ENTRYPOINT ["/bin/sh","./start.sh"]
