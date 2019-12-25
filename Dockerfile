FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PROD 1

# install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apk --no-cache add mariadb-dev jpeg-dev build-base && pip install -U pip && pip install -r requirements.txt && apk del build-base

# copy project
COPY ./ /usr/src/app/
EXPOSE 80
ENTRYPOINT ["./docker/prod_start.sh"]
