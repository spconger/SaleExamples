'''
This class encapsulates a single item with the number
name and price. It is simplified for this example.
It's methods are gets because the values are set
in the __init__ constructor
'''

class Item():

    def __init__(self, itemnum, itemname, itemprice):
        self.itemnum=itemnum
        self.itemname=itemname
        self.itemprice=itemprice

    def getItemNumber(self):
        return self.itemnum

    def getItemName(self):
        return self.itemname
    
    def getItemPrice(self):
        return self.itemprice
    
    def __str__(self):
        return self.itemname