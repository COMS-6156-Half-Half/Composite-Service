from flask import Flask, render_template, session, Blueprint, Response, request
import json
import requests

get_orders_by_seller = Blueprint('get_orders_by_seller', __name__)
@get_orders_by_seller.route('/get_orders_by_seller', methods=["GET", "POST"])
def index():
    URL_user = 'http://ec2-52-91-1-192.compute-1.amazonaws.com:5001/find_user'
    URL_order = 'http://ec2-44-203-155-38.compute-1.amazonaws.com:5000/api/record/seller'

    data = request.get_json()
    seller = str(data["seller"])
    PARAMS_id = {'id': int(seller)}
    # PARAMS_id = json.dumps(PARAMS_id, indent=4)
    r_user = requests.post(url=URL_user, json=PARAMS_id)
    if r_user.status_code == 404:
        return Response("not found user", status=404, content_type="text/plain")
    URL_order = URL_order + '/' + seller
    r = requests.get(url=URL_order)
    if r.status_code == 200:
        return Response(json.dumps(r.json()), status=200, content_type="application.json")
    return Response("not found orders", status=404, content_type="text/plain")