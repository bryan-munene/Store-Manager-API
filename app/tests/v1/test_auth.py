import pytest
from flask import json
from app import create_app
from app.api.v1.views.auth import Users
from app.tests import add_items_helper

testusers = Users()

config = "testing"
app = create_app(config)


#REGISTRATION INPUT FOR TESTS

sample_registration = [
            {
            "name":"",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"pass",
            "password2":"pass"
            },
            {
            "name":"test",
            "email":"",
            "username":"tester2",
            "password":"pass",
            "password2":"pass"
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"",
            "password":"pass",
            "password2":"pass"
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"",
            "password2":"pass"
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"pass",
            "password2":""
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"pass",
            "password2":"pass"
            },
            {
            "name":"test",
            "email":"testmail.com",
            "username":"tester2",
            "password":"pass",
            "password2":"pass"
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"pass",
            "password2":"pass1"
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"pass11",
            "password2":"pass1"
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"pass",
            "password2":"pass"
            },
            {
            "name":"test",
            "email":"test@mail.com",
            "username":"tester2",
            "password":"pass",
            "password2":"pass"
            }
        ]


#LOGIN CREDENTIALS FOR TESTS

sample_login = [
            {
            "email":"",	
            "password":"pass"
            },
            {
            "email":"test@mail.com",	
            "password":""
            },
            {
            "email":"testmail.com",	
            "password":"pass"
            },
            {
            "email":"test@mail.com",	
            "password":"pass"
            },
            {
            "email":"teste@mail.com",	
            "password":"pass1"
            },
            {
            "email":"teste@mail.com",	
            "password":"pass1"
            },
            {
            "email":"test@adminmail.com",	
            "password":"pass"
            }
        ]



'''-------------------------------------------------------------------------------------------------------------------------------'''

#LOGIN TESTS

#INPUT CHECKS

    
def test_login_empty_email():
    result = app.test_client()
    response = result.post('/api/v1/login', data = sample_login[0], content_type = 'application/json')
    assert(response.status_code == 400)

def test_login_empty_password():
    result = app.test_client()
    response = result.post('/api/v1/login', data = sample_login[1], content_type = 'application/json')
    assert(response.status_code == 400)

def test_login_wrong_email_format():
    result = app.test_client()
    response = result.post('/api/v1/login', data = sample_login[2], content_type = 'application/json')
    assert(response.status_code == 400)

def test_login_wrong_email_format2():
    result = app.test_client()
    response = result.post('/api/v1/login', data = sample_login[3], content_type = 'application/json')
    assert(response.status_code == 400)


#CREDENTIALS CHECK

def test_login_wrong_password():
    result = app.test_client()
    response = result.post('/api/v1/login', data = sample_login[4], content_type = 'application/json')
    assert(response.status_code == 400)

def test_login_wrong_email():
    result = app.test_client()
    response = result.post('/api/v1/login', data = sample_login[5], content_type = 'application/json')
    assert(response.status_code == 400)


#CORRECT CREDENTIALS

def test_login_correct_data():
    result = app.test_client()
    response = result.post('/api/v1/login', data = json.dumps(sample_login[6]), content_type = 'application/json')
    json.loads(response.data.decode('utf-8'))
    assert(response.status_code == 200)


'''-------------------------------------------------------------------------------------------------------------------------------'''

#REGISTRATION TESTS

#USER INPUT CHECKS
  
def test_register_empty_name():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[0], content_type = 'application/json')
    assert(response.status_code == 400)

def test_register_empty_email():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[1], content_type = 'application/json')
    assert(response.status_code == 400)

def test_register_empty_username():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[2], content_type = 'application/json')
    assert(response.status_code == 400)

def test_register_empty_password():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[3], content_type = 'application/json')
    assert(response.status_code == 400)

def test_register_empty_password2():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[4], content_type = 'application/json')
    assert(response.status_code == 400)


#EMAIL FORMAT CHECKS

def test_register_wrong_email_format():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[5], content_type = 'application/json')
    assert(response.status_code == 400)

def test_register_wrong_email_format1():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[6], content_type = 'application/json')
    assert(response.status_code == 400)


#PASSWORD CHECK

def test_register_passwords_matching():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[7], content_type = 'application/json')
    assert(response.status_code == 400)

def test_register_passwords_matching1():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[8], content_type = 'application/json')
    assert(response.status_code == 400)


#CORRECT INPUT

def test_register_correct_data():
    result = app.test_client()
    response = result.post('/api/v1/register', data = json.dumps(sample_registration[9]), content_type = 'application/json')
    json.loads(response.data.decode('utf-8'))
    assert (response.status_code == 201)


#DUPLICATE INPUT

def test_register_duplicate_input():
    result = app.test_client()
    response = result.post('/api/v1/register', data = sample_registration[10], content_type = 'application/json')
    assert (response.status_code == 400)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#LOGOUT TESTS

def test_logout_without_logged_in():
    result=app.test_client()
    response= result.get('/api/v1/logout', content_type = 'application/json')
    assert(response.status_code == 200)

def test_logout_correctly():
    result=app.test_client()
    response= result.get('/api/v1/logout', content_type = 'application/json')
    assert(response.status_code == 200)

