import sqlite3
import json
from models import Order, Metal, Size, Style

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
            o.size_id,
            o.style_id,
            o.metal_id,
            m.metal metal_metal,
            m.price metal_price,
            s.style style_style,
            s.price style_price,
            a.carets size_carets,
            a.price size_price
        FROM `Orders` o
        JOIN Metals m 
            ON m.id = o.metal_id
        JOIN Styles s 
            ON s.id = o.style_id
        JOIN Sizes a 
        ON a.id = o.size_id
        """)
        
        orders = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])
            metal = Metal(row['id'], row['metal_metal'], row['metal_price'])
            style = Style(row['id'], row['style_style'], row['style_price'])
            size = Size(row['id'], row['size_carets'], row['size_price'])
            order.metal = metal.__dict__
            order.style = style.__dict__
            order.size = size.__dict__
            
            orders.append(order.__dict__)
    return orders

def get_single_order(id):
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
        WHERE o.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()
        
        order = Order(data['id'], data['metal_id'], data['size_id'], data['style_id'])

    return order.__dict__

def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO "orders"
            ( metal_id, size_id, style_id)
        VALUES
            ( ?, ?, ? );
        """, ( new_order['metal_id'], new_order['size_id'], new_order['style_id'], ))
        
        id = db_cursor.lastrowid
        new_order['id'] = id
    return new_order


def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM "orders"
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break