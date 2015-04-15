FROM ubuntu:trusty
MAINTAINER moosnat@umich.edu

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python-pip python-psycopg2 postgresql libpq-dev python-dev
USER postgres
RUN (service postgresql start &&\
    psql --command "CREATE USER unmute WITH SUPERUSER PASSWORD 'unmute';" &&\
    createdb -O unmute unmute-db)
USER root
RUN useradd app

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD . /app

USER postgres
RUN (service postgresql start &&\
    cd /app &&\
    python -c 'from app import db; db.create_all()')

USER root
RUN chown -R app /app

EXPOSE 5000
WORKDIR /app
CMD ./start.sh
