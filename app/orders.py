ORDERS = {1: [("widget", 2, 9.5)], 2: [("gadget", 1, 20.0), ("bolt", 10, 0.25)]}


def list_orders():
    return [{"id": oid, "lines": len(lines)} for oid, lines in ORDERS.items()]


def order_total(order_id):
    return sum(qty * price for _, qty, price in ORDERS.get(order_id, []))


def order_ids():
    return sorted(ORDERS)
