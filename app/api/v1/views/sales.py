from flask import Blueprint, request, jsonify, make_response, session
from ..models.sales import SalesModel
from ..models.items import ItemsModel

sales_bp = Blueprint('sales', __name__, url_prefix='/api/v1')


sales_model = SalesModel()

class Sales(object):
    @sales_bp.route("/make_sale", methods=["POST"])
    def make_sale():
        if not request.is_json:
            return make_response(
                jsonify({
                    "status": "wrong format",
                    "message": "request not json"
                }), 400)
    
        data = request.get_json()
        payment_mode = data['payment_mode']
        ordered_items = data['sale_items']

        if payment_mode == "":
            return make_response(jsonify({
                "status": "not acceptable",
                "message": "Please fill all the required fields"
            }), 406)

    
        if not len(ordered_items) == 0:
            for ordered_item in ordered_items:
                item_id = ordered_item.get('item_id')
                quantity = ordered_item.get('quantity')

                
                if quantity == "":
                    return make_response(jsonify({
                        "status": "not acceptable",
                        "message": "Please fill all the required fields"
                    }), 406)

                if item_id == "":
                    return make_response(jsonify({
                        "status": "not acceptable",
                        "message": "Please fill all the required fields"
                    }), 406)

                if not quantity.isdigit():
                    return make_response(jsonify({
                        "status": "not acceptable",
                        "message": "Quantity is not valid"
                    }), 400)

                if not item_id.isdigit():
                    return make_response(jsonify({
                        "status": "not acceptable",
                        "message": "Item id is not valid"
                    }), 400)

                
                items_model = ItemsModel()
                items = items_model.get_all()
                if not items:
                    return make_response(jsonify({
                        "status": "not found", 
                        "message": "no items"
                        }), 404)
                                                
                else:
                    for item in items:
                        id = item.get('item_id')
                        if id and id == item_id:
                            name = item.get('name')
                            price = item.get('price')
                            stock_level = item.get('quantity')

                        else:
                            return make_response(jsonify({
                                "status": "not found", 
                                "message": "Item not available"
                            }), 404)
                        
                        if not stock_level:
                            return make_response(jsonify({
                            "status": "not acceptable", 
                            "message": "Item not available"
                            }), 406)
                        else:

                            if int(stock_level) < int(quantity) :
                                return make_response(jsonify({
                                        "status": "not acceptable", 
                                        "message": " we've run out of stock"
                                    }), 406)
                                
                            else:
                                total = int(quantity) * int(price)
                                sales_model.add_sale_items(item_id, name, quantity, price, total)
                                stock_level = int(stock_level) - int(quantity)
                                item['quantity'] = stock_level
                
                grand = 0
                items = 0
                sale_id = sales_model.sale_id
                sale_items = sales_model.get_sale_items_by_sale_id(sale_id)
                
                for sale_item in sale_items:
                    num = sale_item.get('quantity')
                    total = sale_item.get('total')
                    grand = grand + int(total)
                    items = items + int(num)

            sale = sales_model.add_sales(payment_mode, grand, items)
            sales = sales_model.get_all_sales()

            return make_response(jsonify({
                "status": "created",
                "sales": sales,
                "sale_items": sale_items,
                "sale": sale
            }), 201)
        else:
            return make_response(jsonify({
                "status": "not acceptable",
                "message": "You must order atleast one item"
            }), 406)

    @sales_bp.route("/sales", methods=["GET"])
    def sales_all():
        sales = sales_model.get_all_sales()

        if not sales:
            return make_response(jsonify({
                "status": "not found",
                "message": "sales don't exist"
            }), 404)

        else:
            return make_response(jsonify({
                "status": "ok",
                "sales": sales
            }), 200)

    @sales_bp.route('/sales/<int:sale_id>', methods=['GET'])
    def specific_sale(sale_id):
        sale = sales_model.get_sales_by_sale_id(sale_id)

        if not sale:
            return make_response(jsonify({
                "status": "not found",
                "message": "sale you are looking for does not exist"
            }), 404)

        else:
            return make_response(jsonify({
                "status": "ok",
                "sale": sale
            }), 200)
