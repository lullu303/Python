# 가시성
class Product(object):
    pass

class Inventory(object):
    def __init(self):
        self.__items = []

    @property
    def items(self):
        return self.__items
    
my_inventory = Inventory()
items = my_inventory.items
items.append(Product())
# print(items)