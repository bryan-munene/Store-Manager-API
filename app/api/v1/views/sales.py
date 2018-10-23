from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api

sales_bp = Blueprint('sales', __name__,url_prefix='/api/v1')

sales = []
sale_items = []


class Sales(object):
    @sales_bp.route("/make_sale", methods=["POST"])
    def make_sale():
        
        if not request.is_json:
            return make_response(jsonify({"status":"wrong format", "message":"request not json"}),400)
        else:
            data = request.get_json() 
            sale_id =  len(sales)+1
            payment_mode = data['payment_mode']
            ordered_items = data['order_items']
            
            

            
           
        if payment_mode =="":
            return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
        
        else:
            if not len(ordered_items) == 0:
                for ordered_item in ordered_items:
                    item_name = ordered_item.get('item_name')
                    quantity = ordered_item.get('quantity')
                    
                    sale_item_id =  len(sale_items)+1
                    
                    if quantity == "":
                        make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    if item_name == "":
                        make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    
                    if not quantity.isdigit():
                        return make_response(jsonify({"status":"not acceptable", "message":"Quantity is not valid"}),400)
                    if not item_name.isalpha():
                        return make_response(jsonify({"status":"not acceptable", "message":"Food name is not valid"}),400)
                        

                    for item in items:
                        name = item.get('name')
                        price = item.get('price')

                        if item_name == name:
                            total = int(quantity) * int(price)
                            sale_item = {
                                "sale_item_id":sale_item_id,
                                "sale_id":sale_id,
                                "item_name":item_name,
                                "quantity":quantity,
                                "price":price,
                                "total":total
                                }
                            

                            sale_items.append(sale_item)

                    grand = 0
                    items = 0
                    for sale_item in sale_items:
                        id = sale_item.get('sale_id')
                        
                        if id == sale_id:
                            num = sale_item.get('quantity')
                            total = sale_item.get('total')
                            grand = grand + int(total)
                            items = items + int(num)

                sale = {
                    "sale_id":sale_id,
                    "payment_mode":payment_mode,
                    "completed_status":False,
                    "accepted_status":None,
                    "grand_total":grand,
                    "number_of_items":items
                    }

                sales.append(sale)           

                return make_response(jsonify({"status":"created", "sales":sales, "sale_items":sale_items, "sale":sale, "sale_item":sale_item}),201)
            else:
                return make_response(jsonify({"status":"not acceptable", "message":"You must order atleast one item"}),406)


    @sales_bp.route("/sales", methods=["GET"])
    def sales_all():
        
        if len(sales) == 0:
            return make_response(jsonify({"status":"not found","message":"sales don't exist"}),404)
                   
        else:
            return make_response(jsonify({"status":"ok", "sales":sales}),200)
        

