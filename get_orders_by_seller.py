from flask import Flask, render_template, session, Blueprint, Response, request
import json
import requests

get_orders_by_seller = Blueprint('get_orders_by_seller', __name__)
@get_orders_by_seller.route('/get_orders_by_seller', methods=["GET"])
def index():
    URL_user = 'http://projectproduct-env.eba-uninwhdp.us-east-1.elasticbeanstalk.com/search_product'
    URL_order = 'http://projectproduct-env.eba-uninwhdp.us-east-1.elasticbeanstalk.com/search_product'
    data = request.get_json()
    seller = data["seller"]
    PARAMS_id = {'id': seller}
    PARAMS_seller = {'buyer': seller}
    headers = {'Accept': 'application/json'}
    PARAMS_seller = json.dumps(PARAMS_seller, indent=4)
    PARAMS_id = json.dumps(PARAMS_id, indent=4)
    r_user = requests.get(url=URL_user, data=PARAMS_id, headers=headers)
    if r_user.status_code == 404:
        return Response("not found user", status=404, content_type="text/plain")

    r = requests.get(url=URL_order, data=PARAMS_seller, headers=headers)
    if r.status_code == 200:
        return Response(r.json(), status=200, content_type="application.json")

    return Response("not found orders", status=404, content_type="text/plain")