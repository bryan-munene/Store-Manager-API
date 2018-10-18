import pytest
from flask import json
from app import create_app
from app.api.v1.views.items import Items
from app.api.v1.views.sales import Sales


testitems = Items()
testsales = Sales()
app = create_app(config="testing")

#ORDER INPUT FOR TESTS

sample_sale=[{
            "payment_mode":"Cash",
            "sale_items": [
    	                    {
    		                "item_name":"Panadol",
    		                "quantity":"abc"
    	                    },
    	                    {
    		                "item_name":"Amoxil",
    		                "quantity":"def"
    	                    }
                           ]
            },
            {
            "payment_mode":"Cash",
            "sale_items": [
    	                    {
    		                "item_name":"123",
    		                "quantity":"4"
    	                    },
    	                    {
    		                "item_name":"456",
    		                "quantity":"9"
    	                    }
                           ]
            },
            {
            "payment_mode":"Cash",
            "sale_items": [
    	                    {
    		                "item_name":"",
    		                "quantity":"4"
    	                    },
    	                    {
    		                "item_name":"",
    		                "quantity":"9"
    	                    }
                           ]
            },
            {
            "payment_mode":"Cash",
            "sale_items": [
    	                    {
    		                "item_name":"Panadol",
    		                "quantity":""
    	                    },
    	                    {
    		                "item_name":"Amoxil",
    		                "quantity":""
    	                    }
                           ]
            },
            {
            "payment_mode":"Cash",
            "sale_items": [
    	                    {
    		                "item_name":"Panadol",
    		                "quantity":"4"
    	                    },
    	                    {
    		                "item_name":"Amoxil",
    		                "quantity":"9"
    	                    }
                           ]
            },
            {
            "payment_mode":"",
            "sale_items": [
    	                    {
    		                "item_name":"Panadol",
    		                "quantity":"4"
    	                    },
    	                    {
    		                "item_name":"Amoxil",
    		                "quantity":"9"
    	                    }
                           ]
            },
            {
            "payment_mode":"Cash",
            "sale_items": []
            },
            {
            "payment_mode":"Cash",
            "sale_items": [
    	                    {
    		                "item_name":"Panadol",
    		                "quantity":"4"
    	                    },
    	                    {
    		                "item_name":"Amoxil",
    		                "quantity":"9"
    	                    }
                           ]
            }
        ]




'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET ALL SALES TESTS


def test_sales_retrive_all():
    test_client = app.test_client()
    response = test_client.get('/api/v1/sales',content_type='application/json')
    assert(response.status_code==404)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#MAKE A SALE TESTS


def test_sales_quantity_not_digit():
    test_client = app.test_client()
    response = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[0]) ,content_type='application/json')
    assert(response.status_code==400)
    

def test_sales_item_name_not_str():
    test_client = app.test_client()
    response = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[1]) ,content_type='application/json')
    assert(response.status_code==400)
    

def test_sales_item_name_empty():
    test_client = app.test_client()
    response = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[2]) ,content_type='application/json')
    assert(response.status_code==400)
    

def test_sales_quantity_empty():
    test_client = app.test_client()
    response = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[3]) ,content_type='application/json')
    assert(response.status_code==400)
        

def test_sales_payment_method_empty():
    test_client = app.test_client()
    response = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[5]) ,content_type='application/json')
    assert(response.status_code==406)
    

def test_sales_sale_items_empty():
    test_client = app.test_client()
    response = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[6]) ,content_type='application/json')
    assert(response.status_code==406)
    

def test_place_sale_successfully():
    test_client = app.test_client()
    response = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[7]) ,content_type='application/json')
    json.loads(response.data)
    assert(response.status_code==201)
    

'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET SPECIFIC SALE TESTS


def test_get_sale_negative_identifier():
    test_client = app.test_client()
    response = test_client.get('/api/v1/sales/-1' ,content_type='application/json')
    assert(response.status_code == 404)


def test_get_sale_not_created():
    test_client = app.test_client()
    response = test_client.get('/api/v1/sales/100' ,content_type='application/json')
    assert(response.status_code == 404)

def test_get_sale_successfully():
    test_client = app.test_client()
    response = test_client.get('/api/v1/sales/1' ,content_type='application/json')
    assert(response.status_code == 200)

'''-------------------------------------------------------------------------------------------------------------------------------'''

