from flask import Flask, Blueprint


sales_bp = Blueprint('sales', __name__,url_prefix='/api/v1')

sales = []
sale_items = []


class Sales(object):
    @app.route("/api/v1/place_order", methods=["POST", "GET"])
    def make_sale():
        
        if not request.is_json:
            return make_response(jsonify({"status":"wrong format", "message":"request not json"}),400)
        else:
            data = request.get_json() 
            sale_id =  len(sales)+1
            destination = data['destination']
            payment_mode = data['payment_mode']
            ordered_items = data['order_items']
            
            

            
           
        if destination == "" or payment_mode =="":
            return make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
        
        else:
            if not len(ordered_items) == 0:
                for ordered_item in ordered_items:
                    item_name = ordered_item.get('item_name')
                    quantity = ordered_item.get('quantity')
                    
                    order_item_id =  len(sale_items)+1
                    
                    if quantity == "":
                        make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    if item_name == "":
                        make_response(jsonify({"status":"not acceptable", "message":"Please fill all the required fields"}),406)
                    
                    if not quantity.isdigit():
                        return make_response(jsonify({"status":"not acceptable", "message":"Quantity is not valid"}),400)
                    if not food_name.isalpha():
                        return make_response(jsonify({"status":"not acceptable", "message":"Food name is not valid"}),400)
                