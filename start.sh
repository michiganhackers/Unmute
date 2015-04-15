#!/bin/sh

service postgresql start
su app -c "python main.py"
