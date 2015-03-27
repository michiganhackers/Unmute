from __future__ import absolute_import

from flask import Blueprint

blueprint = Blueprint('api', __name__)

from . import views
