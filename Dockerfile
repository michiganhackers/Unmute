FROM ubuntu:trusty
MAINTAINER moosnat@umich.edu

ADD main.py /app/main.py
ADD config.py /app/config.py
ADD app.py /app/app.py
ADD util.py /app/util.py
ADD static /app/static
ADD templates /app/templates
ADD requirements.txt /app/requirements.txt
ADD pages /app/pages
ADD stories /app/stories

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python-pip python-psycopg2 postgresql libpq-dev python-dev
RUN pip install -r /app/requirements.txt
USER postgres
RUN (service postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker unmute-db)
RUN (cd /app && python -c 'from app import db; db.create_all()')

EXPOSE 5000
WORKDIR /app
CMD python main.py
