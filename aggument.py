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

# function closure
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
print(f(5))

# map function 
# explaination: map function takes two arguments, a function and a sequence.
# The function is the first argument and the sequence is the second argument.
# map function applies the function to all the elements of the sequence.
# It returns a new list with the elements changed by the function.

def celciaus(T):
    return (9/5)*T + 32
temp = [0, 22.5, 40, 100]
F = map(celciaus, temp)
print("map function celciaus:",list(F))

# map with lamda
dataMap = [1,2,3,5,6]
datamap1 = [2,3,4,5,6]
result = map(lambda x,y: x+y, dataMap, datamap1)
print("map with lambda:",list(result))

# map with dictionary
dit = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
# map with lambda and sum the points 
result = map(lambda x: {**x, "name":x["name"]+"-gg", "points": x['points']+5}, dit)
print("map with dictionary:",list(result))

# filter function
# filter function takes two arguments, a function and a sequence.
# The function is the first argument and the sequence is the second argument.
# filter function applies the function to all the elements of the sequence.

fltr = filter(lambda x : x['points'] >= 10, dit)
print("filter function:",list(fltr))

# reduce function
# reduce function takes two arguments, a function and a sequence.
# The function is the first argument and the sequence is the second argument.
# reduce function is defined in functools module.
# reduce function applies the function to all the elements of the sequence.

from functools import reduce
red = reduce(lambda acc, x: {'name': acc['name'] + " " + x['name'], 'points': acc['points'] + x['points']}, dit)
print("Reduced dictionary:", [red])




