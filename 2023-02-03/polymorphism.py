# 다형성
    # 같은 이름의 메소드가 다른 기능을 할 수 있도록 하는 것. ex) about_me()

class Animal:
    def __init__(self,name):
        self.name = name
        def talk(self) :
            raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal) :
    def talk(self): # init 함수 생략(부모함수를 가져오겠다.)
        return "Meow!"

class Dog(Animal) :
    def talk (self) :
        return "Woof! Woof!"

animals = [Cat('Missy'), Cat('Mr.Mistofelees'), Dog('Lassie')]
for animal in animals :
    print(animal.name + ':' + animal.talk())