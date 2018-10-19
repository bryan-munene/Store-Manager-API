from flask import Blueprint
from flask_restful import Resource, Api


from instance.config import app_config


v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
