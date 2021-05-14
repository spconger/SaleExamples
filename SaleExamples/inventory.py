'''
The Inventory class consists of a list of item objects.
The Item class is imported
Inventory contains methods for adding an item,
getting the whole item list, and getting an item
by item number.
'''

from item import Item

class Inventory():
    def __init__(self):
        self.items=[]
    
    def addItem(self, i):
        self.items.append(i)

    def getItems(self):
        return self.items
    
    def getItemByNumber(self, number):
        reqItem=None
        for i in self.items:
            if i.itemnum==number:
                reqItem=i
                break
        return reqItem

            