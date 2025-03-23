def test(*a, **b):
    print(a)
    print(b)

test(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5)

# first class function 
# 1. a  can be assigned to a variable
# 2. a can be passed as an argument to a function
# 3. a can be returned from a function
# 4. a can be stored in a data structure such as list, tuple, dictionary, etc.

def circle(x):
    return 3.14* x**2

def func(circle,x):
    return circle(x)

print(func(circle,3))

def add (x, y):
    return x + y
def sub (x, y):
    return x - y

data = [add, sub]
print(data[0])
print(data[0](3, 4))
print(data[1](3, 4))