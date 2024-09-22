#!flask/bin/python
from flask import Blueprint

bp = Blueprint('v1', __name__)

@bp.route('/')
def index():
  return "V1 Home"

