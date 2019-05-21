from item import Item

class Inventory():
    def __init__(self):
        self.items=[]
    
    def addItem(self, i):
        self.items.append(i)
    
    def getItemByNumber(self, number):
        reqItem=None
        for i in self.items:
            if i.itemnum==number:
                reqItem=i
                break
        return reqItem

            