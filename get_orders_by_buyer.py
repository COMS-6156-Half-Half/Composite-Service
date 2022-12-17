from flask import Flask, render_template, session, Blueprint, Response, request
import json
import requests

get_orders_by_buyer = Blueprint("get_orders_by_buyer", __name__)


@get_orders_by_buyer.route("/get_orders_by_buyer", methods=["GET", "POST"])
def index():
    URL_user = "http://ec2-52-91-1-192.compute-1.amazonaws.com:5001/find_user"
    URL_order = "http://ec2-44-203-155-38.compute-1.amazonaws.com:5000/api/record/buyer"
    URL_product = "http://projectproduct-env.eba-uninwhdp.us-east-1.elasticbeanstalk.com/get_product/"

    data = request.get_json()
    buyer = str(data["buyer"])
    PARAMS_id = {"id": int(buyer)}
    # PARAMS_id = json.dumps(PARAMS_id, indent=4)
    r_user = requests.post(url=URL_user, json=PARAMS_id)
    if r_user.status_code == 404:
        return Response("not found user", status=404, content_type="text/plain")
    URL_order = URL_order + "/" + buyer
    r_original = requests.get(url=URL_order)
    r = r_original.json()
    r = list(r)

    for index, i in enumerate(r):
        URL_product_new = URL_product + str(i["product_id"])
        r_product = requests.get(url=URL_product_new)
        i["pname"] = r_product.json()
        PARAMS_id = {"id": int(i["seller_id"])}
        r_user = requests.post(url=URL_user, json=PARAMS_id)
        i["seller_email"] = r_user.json()
        r[index] = i

    if r_original.status_code == 200:
        return Response(json.dumps(r), status=200, content_type="application.json")
    return Response("not found orders", status=404, content_type="text/plain")
