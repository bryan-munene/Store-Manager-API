import pytest
from flask import json
from app import create_app
from app.api.v1.views.items import Items

testitems = Items()
app = create_app(config="testing")


sample_item=[
    {"name":"Hamburger", "price":"abc",	"image":"image"},
    {"name":"Hamburger", "price":"-200",	"image":"image"},
    {"name":"123", "price":"200",	"image":"image"},
    {"name":"", "price":"200",	"image":"image"},
    {"name":"Hamburger", "price":"",	"image":"image"},
    {"name":"Hamburger", "price":"200",	"image":""},
    {"name":"Hamburger", "price":"200",	"image":"image"}
]


sample_item_updates=[
    {"price":"300",	"image":"image1"},
    {"price":"-300",	"image":"image1"},
    {"price":"abc",	"image":"image1"},
    {"price":"300",	"image":""},
    {"price":"",	"image":"image1"},
    {"price":"300",	"image":"image1"},
    {"price":"",	"image":""}
]




'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET ALL ITEMS TESTS


def test_items_retrive_all():
    test_client=app.test_client()
    response= test_client.get('/api/v1/items',content_type='application/json')
    assert(response.status_code==404)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#ADD ITEM TESTS


def test_items_price_not_digit():
    test_client=app.test_client()
    response= test_client.post('/api/v1/add_item', data=sample_item[0] ,content_type='application/json')
    assert(response.status_code==400)

def test_items_price_not_digit1():
    test_client=app.test_client()
    response= test_client.post('/api/v1/add_item', data=sample_item[1] ,content_type='application/json')
    assert(response.status_code==400)

def test_items_item_name_not_str():
    test_client=app.test_client()
    response= test_client.post('/api/v1/add_item', data=sample_item[2] ,content_type='application/json')
    assert(response.status_code==400)

def test_items_item_name_empty():
    test_client=app.test_client()
    response= test_client.post('/api/v1/add_item', data=sample_item[3] ,content_type='application/json')
    assert(response.status_code==400)

def test_items_price_empty():
    test_client=app.test_client()
    response= test_client.post('/api/v1/add_item', data=sample_item[4] ,content_type='application/json')
    assert(response.status_code==400)

def test_items_image_empty():
    test_client=app.test_client()
    response= test_client.post('/api/v1/add_item', data=sample_item[5] ,content_type='application/json')
    assert(response.status_code==400)

def test_items_successfully():
    test_client=app.test_client()
    response= test_client.post('/api/v1/add_item', data=json.dumps(sample_item[6]) ,content_type='application/json')
    json.loads(response.data)
    assert(response.status_code==201)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET SPECIFIC ITEM TESTS


def test_get_item_negative_identifier():
    test_client=app.test_client()
    response= test_client.get('/api/v1/items/-1' ,content_type='application/json')
    assert(response.status_code == 404)

def test_get_item_not_created():
    test_client=app.test_client()
    response= test_client.get('/api/v1/items/100' ,content_type='application/json')
    assert(response.status_code == 404)

def test_get_item_successfully():
    test_client=app.test_client()
    response= test_client.get('/api/v1/items/1' ,content_type='application/json')
    assert(response.status_code == 200)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#UPDATE ITEM TESTS

#FIND ITEM TESTS

def test_update_item_nonexistent():
    test_client=app.test_client()
    response= test_client.put('/api/v1/items/100', data=sample_item_updates[0] ,content_type='application/json')
    assert(response.status_code==400)

def test_items_update_price_not_digit():
    test_client=app.test_client()
    response= test_client.put('/api/v1/add_item', data=sample_item_updates[1] ,content_type='application/json')
    assert(response.status_code==405)

def test_items_update_price_not_digit1():
    test_client=app.test_client()
    response= test_client.put('/api/v1/items/1', data=sample_item_updates[2] ,content_type='application/json')
    assert(response.status_code==400)

def test_update_item_none():
    test_client=app.test_client()
    response= test_client.put('/api/v1/items/1', data=json.dumps(sample_item_updates[6]) ,content_type='application/json')
    assert(response.status_code==406)

def test_update_item_price_only_successfully():
    test_client=app.test_client()
    response= test_client.put('/api/v1/items/1', data=json.dumps(sample_item_updates[3]) ,content_type='application/json')
    assert(response.status_code==200)


def test_update_item_both_successfully():
    test_client=app.test_client()
    response= test_client.put('/api/v1/items/1', data=json.dumps(sample_item_updates[5]) ,content_type='application/json')
    assert(response.status_code==200)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#DELETE SPECIFIC ITEM TESTS


def test_delete_item_negative_identifier():
    test_client=app.test_client()
    response= test_client.delete('/api/v1/items/-1' ,content_type='application/json')
    assert(response.status_code == 404)

def test_delete_item_not_created():
    test_client=app.test_client()
    response= test_client.delete('/api/v1/items/100' ,content_type='application/json')
    assert(response.status_code == 404)

def test_delete_item_successfully():
    test_client=app.test_client()
    response= test_client.delete('/api/v1/items/1' ,content_type='application/json')
    assert(response.status_code == 200)