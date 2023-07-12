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
    return ORDERS

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
