from flask import Flask, Blueprint

from instance.config import app_config

from .api.v1 import v1


def create_app(config):
    '''This function configures the Flask app'''

    app = Flask(__name__)

    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config])
    app.config["TESTING"] = True

    from app.api.v1.views.sales import sales_bp
    app.register_blueprint(sales_bp)
    from app.api.v1.views.items import items_bp
    app.register_blueprint(items_bp)
    from app.api.v1 import v1
    app.register_blueprint(v1)

    return app
