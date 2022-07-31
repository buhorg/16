from flask import request
from config import db, app
from json_data import data_users, data_orders, data_offers
from models import User, Order, Offer
from utils import insert_data_to_model, universal_all_data_handler, universal_data_handler

db.drop_all()
db.create_all()
insert_data_to_model(User, data_users)
insert_data_to_model(Order, data_orders)
insert_data_to_model(Offer, data_offers)


@app.route('/users', methods=['GET', 'POST'])
def users():
    return universal_all_data_handler(User)


@app.route('/users/<int:uid>', methods=['GET', 'PUT', "DELETE"])
def user_search_id(uid):
    return universal_data_handler(User, uid, request.json)


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    return universal_all_data_handler(Order)


@app.route('/orders/<int:uid>', methods=['GET', 'PUT', "DELETE"])
def order_search_id(uid):
    return universal_data_handler(Order, uid, request.json)


@app.route('/offers', methods=['GET', 'POST'])
def offers():
    return universal_all_data_handler(Offer)


@app.route('/offers/<int:uid>', methods=['GET', 'PUT', "DELETE"])
def offer_search_id(uid):
    return universal_data_handler(Offer, uid, request.json)


if __name__ == '__main__':
    app.run(debug=True)
