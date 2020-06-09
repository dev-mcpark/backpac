from app.models import Order
from app.utils import random_number


def make_unique_order_number():
    order_number = random_number(12)
    while Order.objects.filter(order_number=order_number).exists():
        order_number = random_number(12)
    return order_number
