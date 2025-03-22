import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

a = input("Enter a number: ")
b = input("Enter another number: ")

print("Sum: ", add(int(a), int(b)))
print("Difference: ", sub(int(a), int(b)))

print("Square root of", a, "is", math.sqrt(int(a)))

list = [1, 2, 3, 4, 5]
print("Sum of list: ", sum(list))

print("Max of list: ", max(list))
print("Min of list: ", min(list))

print("Factorial of", a, "is", math.factorial(int(a)))

print("Pi: ", math.pi)

print("Euler's number: ", math.e)

print("Log of", a, "is", math.log(int(a)))

print("Log of", a, "base 10 is", math.log10(int(a)))
print("Log of", a, "base 2 is", math.log2(int(a)))

