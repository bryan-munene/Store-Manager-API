from flask import json
import pytest


sample_item = [
    {"name":"Panadol", "price":"200",	"image":"image", "quantity":"12"},
    {"name":"Amoxil", "price":"200",	"image":"image", "quantity":"12"}
]

sample_sale = [{
            "payment_mode":"Cash",
            "sale_items": [
    	                    {
    		                "item_id":"1",
    		                "quantity":"4"
    	                    },
    	                    {
    		                "item_id":"2",
    		                "quantity":"9"
    	                    }
                           ]
            }
]


def add_items_helper(test_client):
    add_item = test_client.post('/api/v1/add_item', data=json.dumps(sample_item[0]) ,content_type='application/json')
    assert(add_item.status_code==201)
    add_item = test_client.post('/api/v1/add_item', data=json.dumps(sample_item[1]) ,content_type='application/json')
    assert(add_item.status_code==201)

def make_sale_helper(test_client):
    add_items_helper(test_client)
    make_sale = test_client.post('/api/v1/make_sale', data=json.dumps(sample_sale[0]) ,content_type='application/json')
    assert(make_sale.status_code==201)
    