#!/usr/bin/env python

import sys
from app import app

if __name__=='__main__':
    app.run(host="0.0.0.0", threaded=True)

