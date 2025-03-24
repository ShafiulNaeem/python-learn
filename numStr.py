# number type
# int, float, complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(float(x))
print(int(y))
print(complex(x))

# random number
import random
print(random.randrange(100, 1000))

# string type
# single line string
a = "single line string"
# ADD NEW LINE before print
print("\n"+ a)

# multi line string
b = """APPLE,
BANANA,
CHERRY
"""
print(b)

# string array
print(a[1])

# loop through string
for x in "banana":
    print(x)

# string length
print(len(a))
# check string

if "APPLE" in b:
    print("Yes, 'apple' is in the fruits string")

# format string
age = 27
ageMonth = age * 12
txt = f"My name is \"Rifat\", and I am {age:.2f}"+" years old. I am {} months old".format(ageMonth)
text = "My name is Rifat, and I am {} years old. I am {} months old".format( 20,30)
print(text)
print(txt)

