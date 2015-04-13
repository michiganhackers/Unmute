from __future__ import absolute_import

from flask import Blueprint

blueprint = Blueprint('pages', __name__)

from . import views
