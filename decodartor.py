# functions decodartor
print("=== functions decodartor ===")

def my_decorator(func):
    def new(a, b):
        print("Code before the function a + b:", a+b)
        func(a,b)
        print("Code after the function a-b:", a-b)
    return new

# a = input("Enter the value of a:")
# b = input("Enter the value of b:")
@my_decorator
def multi(a, b):
    print("The mul of a*b:", a*b)

multi(int(3), int(3))

# method decorators
print("=== method decorators ===")
class Math:
    def method_decorator(func):
        def new(self, a, b):
            print("Code before the function a + b:", a+b)
            data = func(self, a, b)
            print("Code after the function a-b:", data*data)
        return new
    @method_decorator
    def multi(self, a, b):
        return a*b
    
m = Math()
m.multi(3, 3)

# class decorators
print("=== class decorators ===")
def class_decorator(func):
    # print(list(func.__dict__.items()))
    # for key, value in func.__dict__.items():
    #     print(key, value)
    
    func.class_name = func.__name__
    func.age = 20
    func.name = "Rifat Naeem"
    return func
    

@class_decorator
class Math:
    name = "Rifat"
    age = 10
    def __init__(self):
        print("This is a class decorator")
    
    @staticmethod
    def multi(a, b):
        return a*b
    @classmethod
    def get_month_age(self,hh):
        self.age = self.age *12
        return self.age
    
    @property
    def get_age_day(self):
        return self.age
    
    @get_age_day.setter
    def get_age_day(self,value):
        self.age = value*365
    
    
m = Math()
print(m.class_name)
print(m.age)
print(m.name)
# property decorators
print("=== property decorators ===")
m.get_age_day = m.age
print(m.get_age_day)
#  static method decorators
print("=== static method decorators ===")
print(Math.multi(3, 3))

# class method decorators
print("=== class method decorators ===")
print(Math.age)
Math.get_month_age(6)
print(Math.age)

# chaining decorators
print("=== chaining decorators ===")
def test1(func):
    def new():
        x = func()
        return x + 1
    return new

def test2(func):
    def new():
        x = func()
        return x * 2
    return new

@test1
@test2
def test():
    return 10

print(test())





