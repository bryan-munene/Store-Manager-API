from flask import Blueprint, request, jsonify, make_response, session
import re
from ..models.auth import UserModel

from app.api.v1.utility.validators import json_checker


users_bp = Blueprint('users', __name__, url_prefix='/api/v1')

user_model = UserModel()

class Users(object):
    @users_bp.route("/login")
    def home():
        if session.get('logged_in'):
            return make_response(jsonify({
                "status": "user logged in",
                "username": session['username'],
                "login": True
            }), 200)
        elif session.get('logged_in_admin'):
            return make_response(jsonify({
                "status": "admin logged in",
                "username": session['username'],
                "login": True
            }), 200)
        else:
            return make_response(jsonify({
                "status": "login error",
                "login": False
            }), 401)

    @users_bp.route("/login", methods=["POST"])
    def do_user_login():
        json_checker(request)
        data = request.get_json()
        email = data['email']
        password = data['password']
    
        if email == "" or password == "":
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Please fill all required fields"
            }), 406)

        if not re.match(
            "^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$",
                email, re.IGNORECASE):
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Email Provided is not in email format"
            }), 406)
        users = user_model.get_all()
        for user in users:
            user_email = user.get('email')
            user_password = user.get('password')
            user_role = user.get('is_admin')
            if password == user_password and email == user_email and not user_role:
                session['username'] = user.get('username')
                session['logged_in'] = True
                return Users.home()
            elif password == user_password and email == user_email and user_role:
                session['username'] = user.get('username')
                session['logged_in_admin'] = True
                return Users.home()
            else:
                session['logged_in'] = False
                session['logged_in_admin'] = False

        return Users.home()

    @users_bp.route("/register", methods=["POST"])
    def register():
        if not session.get('logged_in_admin'):
            return make_response(jsonify({
                "status": "unauthorised",
                "message": "Admin User must be logged in"
            }), 401)

        if not request.is_json:
            return make_response(jsonify({
                "status": "wrong format",
                "messenge": "request not json"
            }), 400)
        else:
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

        if name == "" or email == "" or usrnm == "" or pswrd == "" or pswrd2 == "":
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Please fill all the required fields"
            }), 406)

        if not re.match(
            "^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$",
                email, re.IGNORECASE):
            return make_response(jsonify({
                "status": "not acceptable",
                "messenge": "Email Provided is not in email format"
            }), 406)
        
        users = user_model.get_all()
        if len(users) > 0:
            for user in users:
                user_email = user.get('email')

                if email == user_email:
                    return make_response(jsonify({
                        "status": "not acceptable",
                        "messenge": "user already exists"
                    }), 406)

                else:
                    user = user_model.add_user(name, email, usrnm, pswrd, is_admin)
                    return make_response(jsonify({
                        "status": "created",
                        "user": user,
                        "users": users
                        }), 201)

        user = user_model.add_user(name, email, usrnm, pswrd, is_admin)
        
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
        if len(users) == 0:
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
