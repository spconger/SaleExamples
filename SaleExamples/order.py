'''
This class processes the order. It contains a list of 
orderitem objects. It is quite simplified. I did not calculate
tax or any discounts.
'''

from item import Item
from orderitem import OrderItem
from payment import Payment

class Order():
    def __init__(self):
        self.orderitems=[]

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def getOrderItems(self):
        return self.orderitems

    def calcTotal(self):
        total=0.0
        for o in self.orderitems:
            total += o.getItem().itemprice * o.quantity
        payment=Payment(total)
        return payment

    