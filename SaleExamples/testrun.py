from item import Item
from orderitem import OrderItem
from order import Order
from payment import Payment
from inventory import Inventory

def main():

    item1=Item(1,'beer', 10.00)
    item2=Item(2,'chips', 3.00)
    item3=Item(3,'salsa', 2.00)

    inventory=Inventory()
    inventory.addItem(item1)
    inventory.addItem(item2)
    inventory.addItem(item3)

    orderitem1=OrderItem(inventory.getItemByNumber(1),1)
    orderitem2=OrderItem(inventory.getItemByNumber(2),3)
    orderitem3=OrderItem(inventory.getItemByNumber(3),2)

    order = Order()
    order.addOrderItems(orderitem1)
    order.addOrderItems(orderitem2)
    order.addOrderItems(orderitem3)

    payment =order.calcTotal()
    print(payment)

main()