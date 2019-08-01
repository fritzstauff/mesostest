FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install curl wget
COPY ./app /app
