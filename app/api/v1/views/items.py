from flask import Flask, Blueprint


items = Blueprint('items', __name__,url_prefix='/api/v1')


class Items(object):
    pass