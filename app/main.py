from flask import Flask, jsonify

from app.orders import list_orders, order_total

app = Flask(__name__)


@app.get("/orders")
def orders():
    return jsonify(list_orders())


@app.get("/orders/<int:order_id>/total")
def total(order_id: int):
    return jsonify({"order_id": order_id, "total": order_total(order_id)})
