from flask import Blueprint, request, jsonify, make_response


items_bp = Blueprint('items', __name__, url_prefix='/api/v1')


items = []


class Items(object):
    @items_bp.route("/")
    def index():
        return jsonify(200,"WELCOME. You are here.")

    @items_bp.route('/add_item', methods=["POST"])
    def add_items():
        
        if not request.is_json:
            return make_response(jsonify({"status":"wrong format","messenge":"request not json"}),400)
        else:
            data = request.get_json() 
            item_id =  len(items)+1
            name = data['name']
            price = data['price']
            image = data['image']
            quantity = data['quantity']
            
        if name == "" or price == "" or image == "" or quantity =="":
            return make_response(jsonify({"status":"not acceptable","message":"all fields must be filled"}),406)

        if not price.isdigit():
            return make_response(jsonify({"status":"not acceptable","message":"price not valid"}),405)

        if not name.isalpha():
            return make_response(jsonify({"status":"not acceptable","message":"item name not valid"}),405)

        
        

        if len(items) > 0:
            for item in items:
                item_name = item.get('name')
                item_price = item.get('price')
                
            if name == item_name and price == item_price:
                return make_response(jsonify({"status":"forbidden","message":"item already exists"}),403)
           
            else:
                item = {
                    "item_id":item_id,
                    "name":name,
                    "price":price,   
                    "image":image,
                    "quantity":quantity
                    }

                
                
        else:
            item = {
                    "item_id":item_id,
                    "name":name,
                    "price":price,   
                    "image":image,
                    "quantity":quantity
                    }

        items.append(item)

        return make_response(jsonify({"status":"created", "item":item, "items":items }),201)
            
                
    
    @items_bp.route("/items", methods=["GET"])
    def items_all():
        if len(items) == 0:
            return make_response(jsonify({"status":"not found","message":"items you are looking for does not esxist"}),404)
        else:
            return make_response(jsonify({"status":"ok", "items":items}),200)


    
    @items_bp.route('/items/<int:item_id>', methods=['GET'])
    def specific_item(item_id):        
        if len(items) != 0:
            for item in items:
                id = item.get('item_id')
                while id == item_id:
                    return make_response(jsonify({"status":"ok", "item":item}),200)
            else:
                return make_response(jsonify({'error':'the item does not exist'}),404)

        

        else:
            return make_response(jsonify({'error':'the item does not exist'}),404)

    
class gets(object):
    def get_item(self):        
        return items
        
            