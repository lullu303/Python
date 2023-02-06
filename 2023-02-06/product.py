class Product(object):
    pass    # 비어있는 클래스 하나 만든다 = 생략

class Inventory(object):
    def __init__(self):
        self.__items = [] # 클래스 내부에서만 판단할 수 있음.
        # self.items = []

    def add_new_item(self,product):
        if type(product) == Product:
            self.__items.append(product)    #대문자 product랑 같으면 추가시킬게.
            print("new item added")
        else:
            raise ValueError("Invaild Item")
        
    def get_number_of_items(self):
        return len(self.__items)    #list에 몇개가있는지 세어서 출력.
    
my_inventory = Inventory()  # Inventory객체가 my_inventory에 담김
my_inventory.add_new_item(Product())    #Product 인스턴스 아이템을 추가
my_inventory.add_new_item(Product())
print(my_inventory.get_number_of_items())
# my_inventory.__items # AttributeError: 'Inventory' object has no attribute '__items'
# my_inventory.items # AttributeError: 'Inventory' object has no attribute 'items'
# 정보은닉을 했기 때문.



