from item import Item
from orderitem import OrderItem
from order import Order
from payment import Payment
from inventory import Inventory

def main():

    item1=Item(1,'soap', 2.25)
    item2=Item(2,'cookies', 5.00)
    item3 =Item(3,'milk', 2.25)

    inventory=Inventory()
    inventory.addItem(item1)
    inventory.addItem(item2)
    inventory.addItem(item3)

    orderitem1=OrderItem(inventory.getItemByNumber(1),1)
    orderitem2=OrderItem(inventory.getItemByNumber(2),2)
    orderitem3=OrderItem(inventory.getItemByNumber(3),1)

    order = Order()
    order.addOrderItems(orderitem1)
    order.addOrderItems(orderitem2)
    order.addOrderItems(orderitem3)

    payment =order.calcTotal()
    print(payment)

main()