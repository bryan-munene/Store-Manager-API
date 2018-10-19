from flask import Flask, Blueprint


sales_bp = Blueprint('sales', __name__,url_prefix='/api/v1')


class Sales(object):
    pass