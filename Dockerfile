FROM ubuntu:trusty
MAINTAINER moosnat@umich.edu

ADD . /app

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python-pip python-psycopg2 postgresql libpq-dev python-dev
RUN pip install -r /app/requirements.txt
USER postgres
RUN (service postgresql start &&\
    psql --command "CREATE USER unmute WITH SUPERUSER PASSWORD 'unmute';" &&\
    createdb -O unmute unmute-db)
RUN (service postgresql start &&\
    cd /app &&\
    python -c 'from app import db; db.create_all()')

EXPOSE 5000
WORKDIR /app
CMD python main.py
