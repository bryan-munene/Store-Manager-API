from flask import make_response, jsonify, json
import re

def json_checker(request):
    '''
    this function checks if the request object is in json form
    '''
    if not request.is_json:
        return False
    return True

def blanks_login(email, password):
    if email:
        if email == "":
            return False
        return True
    
    
    if password:
        if password == "":
            return False
        return True
    
   


def blanks_reistration(name, email, usrnm, pswrd, pswrd2):
    if name:
        if name =="":
            return False
        return True
    

    if email:
        if email =="":
            return False
        return True
    

    if usrnm:
        if usrnm == "":
            return False
        return True
    
    
    if pswrd:
        if pswrd =="":
            return False
        return True
    

    if pswrd2:
        if pswrd2 =="":
            return False
        return True
    
            


def email_checker(email):
    if not re.match(
        "^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$",
            email, re.IGNORECASE):
        return False
    return True
