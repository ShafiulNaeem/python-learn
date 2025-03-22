class Person:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def calculateMonths(self):
        return self.age * 12



data = Person('John', 25)
print(data.name)
print(data.age)
print("output:", data) 
print(data.calculateMonths()) 
