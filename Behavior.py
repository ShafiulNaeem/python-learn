
from Person import Person
from oop.Main import Main

class Behavior(Person,Main):
    behave = None
    def __init__(self, name, age, behave):
        super().__init__(name, age)
        self.behave = behave
    
    def __str__(self):
        return f"{super().__str__()}, Behavior: {self.behave}"

data = Behavior('John', 25, 'Good')
print(data)
print(data.calculateMonths())
print(data.test())