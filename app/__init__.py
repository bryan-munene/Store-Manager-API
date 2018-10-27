import os
from flask import Flask, Blueprint
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

from instance.config import app_config

from .api.v1 import v1


jwt = JWTManager()

def create_app(config):
    '''This function configures the Flask app'''


    app = Flask(__name__)

    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config])
    app.config["TESTING"] = True

    app.config["JWT_SECRET_KEY"]= os.urandom(12)

    jwt.init_app(app)
    
    app.secret_key = os.urandom(12)

    from app.api.v1.views.sales import sales_bp
    app.register_blueprint(sales_bp)
    from app.api.v1.views.items import items_bp
    app.register_blueprint(items_bp)
    from app.api.v1.views.auth import users_bp
    app.register_blueprint(users_bp)


    from app.api.v1 import v1 as v1
    app.register_blueprint(v1)

    return app
