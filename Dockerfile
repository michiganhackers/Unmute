FROM ubuntu:trusty

ADD *.py /app/
ADD static /app/static
ADD templates /app/templates
ADD requirements.txt /app/requirements.txt
ADD pages /app/pages
ADD stories /app/stories

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python-pip python-psycopg2 postgresql libpq-dev python-dev
RUN pip install -r /app/requirements.txt
RUN (cd /app && python -c 'from app import db; db.create_all()')

WORKDIR /app
CMD python main.py
