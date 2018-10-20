from flask import Blueprint, request, jsonify, make_response, session
from .items import gets
from .auth import Users

auth = Users()

items_find = gets()

sales_bp = Blueprint('sales', __name__, url_prefix='/api/v1')

sales = []
sale_items = []


class Sales(object):
    @sales_bp.route("/make_sale", methods=["POST"])
    def make_sale():
        if not session.get('logged_in'):
            return make_response(jsonify({
                "status": "unauthorised",
                "message": "Admin User must be logged in"
            }), 401)

        if not request.is_json:
            return make_response(
                jsonify({
                    "status": "wrong format",
                    "message": "request not json"
                }), 400)
        else:
            data = request.get_json()
            sale_id = len(sales) + 1
            payment_mode = data['payment_mode']
            ordered_items = data['sale_items']

        if payment_mode == "":
            return make_response(jsonify({
                "status": "not acceptable",
                "message": "Please fill all the required fields"
            }), 406)

        else:
            if not len(ordered_items) == 0:
                for ordered_item in ordered_items:
                    item_id = ordered_item.get('item_id')
                    quantity = ordered_item.get('quantity')

                    sale_item_id = len(sale_items) + 1

                    if quantity == "":
                        make_response(jsonify({
                            "status": "not acceptable",
                            "message": "Please fill all the required fields"
                        }), 406)

                    if item_id == "":
                        make_response(jsonify({
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
                            "message": "Food id is not valid"
                        }), 400)

                    '''
                    for item in items:
                        name = item.get('name')
                        price = item.get('price')
                    '''

                    items = items_find.get_item()
                    for item in items:
                        # return make_response(jsonify({"status":"ok",
                        # "item":item}),200)

                        id = item.get('item_id')
                        

                        if int(id) == int(item_id):
                            # return make_response(jsonify({"status":"ok",
                            # "item":item, "item_id":item_id, "id":id}),200)

                            name = item.get('name')
                            price = item.get('price')
                            stock_level = item.get('quantity')

                            if int(stock_level) > int(quantity):

                                total = int(quantity) * int(price)

                                sale_item = {
                                    "sale_item_id": sale_item_id,
                                    "sale_id": sale_id,
                                    "item_id": item_id,
                                    "item_name": name,
                                    "quantity": quantity,
                                    "price": price,
                                    "total": total
                                }

                                sale_items.append(sale_item)

                                stock_level = int(stock_level) - int(quantity)

                                item['quantity'] = stock_level
                            
                            else:
                                return make_response(jsonify({
                                    "status": "not acceptable", 
                                    "message": "Stock levels not enough"
                                    }), 406)


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
                    "sale_id": sale_id,
                    "payment_mode": payment_mode,
                    "grand_total": grand,
                    "number_of_items": items
                }

                sales.append(sale)

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
        if not session.get('logged_in_admin'):
            return make_response(jsonify({
                "status": "unauthorised",
                "message": "Admin User must be logged in"
            }), 401)

        if len(sales) == 0:
            return make_response(jsonify({
                "status": "not found",
                "message": "sales don't exist"
            }), 404)

        else:
            return make_response(jsonify({
                "status": "ok",
                "sales": sales
            }), 200)

    @sales_bp.route('/orders/<int:sale_id>', methods=['GET'])
    def specific_sale(sale_id):
        if not session.get('logged_in_admin'):
            return make_response(jsonify({
                "status": "unauthorised",
                "message": "Admin User must be logged in"
            }), 401)

        sale = [sale for sale in sales if sale.get('sale_id') == sale_id]

        if len(sale) == 0:
            return make_response(jsonify({
                "status": "not found",
                "message": "sale you are looking for does not exist"
            }), 404)

        else:
            return make_response(jsonify({
                "status": "ok",
                "sale": sale
            }), 200)
