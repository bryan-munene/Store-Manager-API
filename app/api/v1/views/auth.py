from flask import Blueprint, request, jsonify, make_response


users_bp = Blueprint('users', __name__, url_prefix='/api/v1')


users = [{
        "is_admin":True,
        "email":"test@adminmail.com",
        "name":"test",
        "password":"pass",
        "user_id":1,
        "username":"tester"
    }]


class Users(object):
    pass
