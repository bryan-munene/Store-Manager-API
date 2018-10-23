from flask import make_response, jsonify, json

def json_checker(request):
    if not request.is_json:
        return make_response(
            jsonify({
                "status": "wrong format",
                "message": "request not json"
            }), 400)

