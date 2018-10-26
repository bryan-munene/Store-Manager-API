from flask import Blueprint, request, jsonify, make_response, session
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from datetime import datetime

from ..models.auth import UserModel
from app.api.v1.utility.validators import json_checker, blanks_login, blanks_reistration, email_checker



users_bp = Blueprint('users', __name__, url_prefix='/api/v1')

user_model = UserModel()

class Users(object):
    @users_bp.route("/login", methods=["POST"])
    def user_login():
        ok = json_checker(request)
        if not ok:
            return make_response(jsonify({
                "status": "wrong format",
                "messenge": "request not json"
            }), 400)

        data = request.get_json()
        email = data['email']
        password = data['password']
        
        filled = blanks_login(email, password)
        if not filled:
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Please fill all required fields"
            }), 406)
        
        Email = email_checker(email)
        if not Email:
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Email Provided is not in email format"
            }), 406)

        user = user_model.get_user_by_email(email)
        if user:
            user_password = user.get('password')
            user_role =user.get('is_admin')
        else:
            return make_response(jsonify({
                "status": "not found",
                "messenge": "User does not exist"
            }), 404)

        credentials = user_model.check_password(user_password, password)
        '''exp = datetime.timedelta(minutes=15)
'''
        if credentials and not user_role:
            token = create_access_token(user['email'])
            return make_response(jsonify({
                "status": "user logged in",
                "username": user['username'],
                "login": True,
                "token": token
                }), 200)

        elif credentials and user_role:
            token = create_access_token(user['email'])
            return make_response(jsonify({
                "status": "Admin logged in",
                "username": user['username'],
                "login": True,
                "token": token
                }), 200)
        else:
            return make_response(jsonify({
                "status": "login error",
                "login": False
                }), 401)

    @users_bp.route("/register", methods=["POST"])
    def register():
        if not session.get('logged_in_admin'):
            return make_response(jsonify({
                "status": "unauthorised",
                "message": "Admin User must be logged in"
            }), 401)

        ok = json_checker(request)
        if not ok:
            return make_response(jsonify({
                "status": "wrong format",
                "messenge": "request not json"
            }), 400)
        
        data = request.get_json()
        name = data['name']
        email = data['email']
        usrnm = data['username']
        pswrd = data['password']
        pswrd2 = data['password2']
        is_admin = False

        if not pswrd == pswrd2:
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "passwords don't match"
            }), 406)

        inputs = blanks_reistration(name, email, usrnm, pswrd, pswrd2)
        if not inputs:
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Please fill all the required fields"
            }), 406)

        Email = email_checker(email)
        if not Email:
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Email Provided is not in email format"
            }), 406)

        user = user_model.get_user_by_email(email)
        if user:
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "user already exists"
                }), 406)

        else:
            user = user_model.add_user(name, email, usrnm, pswrd, is_admin)
            users = user_model.get_all()
            return make_response(jsonify({
                "status": "created",
                "user": user,
                "users": users
                }), 201)


    @users_bp.route("/logout")
    def logout():
        if session.get('logged_in') or session.get('logged_in_admin'):
            session['logged_in'] = False
            session['logged_in_admin'] = False
            return make_response(jsonify({
                "status": "okay",
                "messenge": "user logged out"
            }), 200)

        else:
            return make_response(jsonify({
                "status": "okay",
                "messenge": "user must be logged in"
            }), 400)

    @users_bp.route("/users", methods=["GET"])
    def users_all():
        if not session.get('logged_in_admin'):
            return make_response(jsonify({
                "status": "unauthorised",
                "message": "Admin User must be logged in"
            }), 401)
        users = user_model.get_all()
        if not users:
            return make_response(jsonify({
                "status": "not found",
                "message": "users you are looking for do not esxist"
            }), 404)
        else:
            return make_response(
                jsonify({
                    "status": "ok",
                    "users": users
                }), 200)
