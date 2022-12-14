from flask import Flask, redirect, url_for, session
from get_orders_by_buyer import get_orders_by_buyer
from flask import Blueprint


app = Flask(__name__)
app.secret_key = '12345678'


app.register_blueprint(get_orders_by_buyer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)