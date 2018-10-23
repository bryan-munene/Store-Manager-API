from flask import Flask

from instance.config import app_config

from .api.v1.views.sales import sales
from .api.v1.views.items import items


def create_app(config):
    '''This function configures the Flask app'''
    
    app = Flask(__name__)
    
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config])
    app.config["TESTING"] = True


    app.register_blueprint(sales)
    app.register_blueprint(items)


    return app