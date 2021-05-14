'''
This class tests the methods of the classes
in this sales example. The setUp method provides
an instance of the class and values to test
against.
'''

import unittest
from item import Item
from inventory import Inventory
from orderitem import OrderItem
from order import Order
from payment import Payment

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(1,'beer',12.95)

    def test_itemString(self):
        self.assertEqual(str(self.item),self.item.itemname)

    def test_getPrice(self):
        self.assertEqual(str(self.item.getItemPrice()), '12.95')

    def test_getItemNumber(self):
        self.assertEqual(str(self.item.getItemNumber()),'1')

class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.item1=Item(1,'beer', 12.95)
        self.item2=Item(2,'chips', 4.75)
        self.item3=Item(3,'salsa', 2.75)

        #add items
        self.inven=Inventory()
        self.inven.addItem(self.item1)
        self.inven.addItem(self.item2)
        self.inven.addItem(self.item3)
       
    
    def test_getItems(self):
                
        items=self.inven.getItems()
        self.assertEqual(len(items), 3)

    def test_getItemByNumber(self):
        item=self.inven.getItemByNumber(2)
        self.assertEqual(str(item),'chips')


class OrderItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(1,'salsa', 2.75)
        self.quantity=2
        self.orderitem=OrderItem(self.item, self.quantity)

    def test_getItem(self):
        self.item = self.orderitem.getItem()
        self.assertEqual(str(self.item),'salsa')

    def test_getItemPriceFromOrderItem(self):
        self.item = self.orderitem.getItem()
        self.assertEqual(self.item.getItemPrice(), 2.75)

    def test_getQuantity(self):
        self.assertEqual(self.orderitem.getQuantity(),2)


class OrderTest(unittest.TestCase):

   def setUp(self):
       self.o=Order()
       self.item1=Item(1,'beer', 10.00)
       self.item2=Item(2,'chips', 3.00)
       self.item3=Item(3,'salsa', 2.00)

       self.orderitem1=OrderItem(self.item1,1)
       self.orderitem2=OrderItem(self.item2,3)
       self.orderitem3=OrderItem(self.item3,2)

       
       self.o.addOrderItems(self.orderitem1)
       self.o.addOrderItems(self.orderitem2)
       self.o.addOrderItems(self.orderitem3)

   def test_addandGetOrderItems(self):
    
       self.oitems=self.o.getOrderItems()
       self.assertEqual(len(self.oitems),3)

   def test_CalculateTotal(self):
        payment=self.o.calcTotal()
        self.assertEqual(str(payment), 'Your payment today will be 23.0')




