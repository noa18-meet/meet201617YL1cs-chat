from abc import ABCMeta,abstractmethod
class Animal(metaclass=ABCMeta):

    def eat(self):
        print('YUM!')

    @abstractmethod
    def run(self):
        pass

# When we inherit from an abstract class we need
# to implement all its abstract methods


class Dog(Animal):
    
    def __init__(self):
        print('hi')
    def bark (self):
        print ("waf")
    def run(self):
        print("tunning!")
    def wawa(self):
        print('wawa')
    

d = Dog()
##d.bark()
##d.eat()
##d.run()
    
