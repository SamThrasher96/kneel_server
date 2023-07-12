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