'''
An order item encapsulates an item but adds a quantity
This could also be done as inheritance

'''

from item import Item

class OrderItem():
    def __init__(self,item, quantity):
        self.item=item
        self.quantity=quantity

    def getItem(self):
        return self.item
    
    def getQuantity(self):
        return self.quantity