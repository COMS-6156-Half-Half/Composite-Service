from flask import Flask, render_template, session, Blueprint, Response, request
import json
import requests

get_orders_by_buyer = Blueprint('get_orders_by_buyer', __name__)
@get_orders_by_buyer.route('/get_orders_by_buyer', methods=["GET"])
def index():
    URL_user = 'http://127.0.0.1:5001/find_user'
    URL_order = 'http://projectproduct-env.eba-uninwhdp.us-east-1.elasticbeanstalk.com/search_product'

    data = request.get_json()
    buyer = data["buyer"]
    PARAMS_id = {'id': buyer}
    PARAMS_buyer = {'buyer': buyer}
    headers = {'Accept': 'application/json'}
    PARAMS_buyer = json.dumps(PARAMS_buyer, indent=4)
    PARAMS_id = json.dumps(PARAMS_id, indent=4)
    r_user = requests.get(url=URL_user, data=PARAMS_id, headers = headers)
    if r_user.status_code == 404:
        return Response("not found user", status=404, content_type="text/plain")

    r = requests.get(url = URL_order, data= PARAMS_buyer, headers = headers)
    if r.status_code == 200:
        return Response(r.json(), status=200, content_type="application.json")
    return Response("not found orders", status=404, content_type="text/plain")