from flask import Blueprint, request, jsonify, make_response, session
from ..models.items import ItemsModel

items_model = ItemsModel()

items_bp = Blueprint('items', __name__, url_prefix='/api/v1')



@items_bp.route("/")
def index():
    return jsonify(200, "WELCOME. You are here.")


class Items(object):
    @items_bp.route('/add_item', methods=["POST"])
    def add_items():
        if not request.is_json:
            return make_response(
                jsonify({
                    "status": "wrong format",
                    "messenge": "request not json"
                }), 400)
    
        data = request.get_json()
        name = data['name']
        price = data['price']
        image = data['image']
        quantity = data['quantity']

        if name == "" or price == "" or image == "" or quantity == "":
            return make_response(jsonify({
                "status": "not acceptable",
                "message": "all fields must be filled"
            }), 406)

        if not price.isdigit():
            return make_response(
                jsonify({
                    "status": "not acceptable",
                    "message": "price not valid"
                }), 405)

        if not name.isalpha():
            return make_response(
                jsonify({
                    "status": "not acceptable",
                    "message": "item name not valid"
                }), 405)

        item = items_model.get_by_name_and_price(name, price)
        if item:
            return make_response(
                jsonify({
                    "status": "forbidden",
                    "message": "item already exists"
                    }), 403)

        item = items_model.add_item(name, price, image, quantity)
        items = items_model.get_all()
        return make_response(
            jsonify({
                "status": "created",
                "item": item,
                "items": items
            }), 201)

    @items_bp.route("/items", methods=["GET"])
    def items_all():
        items = items_model.get_all()
        if not items:
            return make_response(jsonify({
                "status": "not found",
                "message": "items you are looking for does not esxist"
            }), 404)
        else:
            return make_response(
                jsonify({
                    "status": "ok",
                    "items": items
                }), 200)

    @items_bp.route('/items/<int:item_id>', methods=['GET'])
    def specific_item(item_id):
        item = items_model.get_by_id(item_id)
        if item:
            return make_response(
                jsonify({
                    "status": "ok",
                    "item": item
                }), 200)
        else:
            return make_response(
                jsonify({
                    'error': 'the item does not exist'
                }), 404)
