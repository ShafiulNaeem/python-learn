try:
    x = 1
    print(x/1)
    value = int(input("Enter a number: "))
except Exception as e:
    print("Error:",e)
else:
    print("No exception")
finally:
    print("Finally block")