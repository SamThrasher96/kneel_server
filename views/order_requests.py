import sqlite3
import json
from models import Order

ORDERS = [
    {
        "metalId": 1,
        "sizeId": 4,
        "styleId": 2,
        "id": 1
    },
    {
        "metalId": 3,
        "sizeId": 5,
        "styleId": 3,
        "id": 2
    }
]

def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM "orders" o
        """)
        
        orders = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])
            orders.append(order.__dict__)
    return orders

def get_single_order(id):
    requested_orders = None
    for order in ORDERS:
        if order["id"] == id:
            requested_orders = order
    return requested_orders

def create_order(order):
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def delete_order(id):
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break