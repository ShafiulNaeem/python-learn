# lamda start
print("=== lamda start ===")
# lambda function
add = lambda x, y: x + y
print(add(5, 3))

# lambda with sort
data = [1,2,3,4,5,6,7,8,9,10]
data.sort(key=lambda x: x % 2)
print("sort:",data)

# lambda with filter
data = [1,2,3,4,5,6,7,8,9,10]
def evenFn(x):
    return x % 2 == 0
even = filter(evenFn, data)
# even = list(filter(lambda x: x % 2 == 0, data))
print("even:",list(even))

# lambda with map
def doubleFn(x):
    return x * 2
double = map(doubleFn, data)
for i in double:
 print("double:",i)