from abc import ABC,abstractmethod
class Animal(ABC):
    # property decorator is used to access the method like an attribute
    @property
    @abstractmethod
    def color(self):
        pass
    #  abstract method is used to define the method in the child class
    @abstractmethod
    def sound(self):
        pass

    # concreate method is used to define the method in the parent class
    def eat(self):
        return "I eat food"
    