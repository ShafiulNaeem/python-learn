data = ["Rifat", 28, "Dhaka", 5.6, "Python", True]
strList = ["Rifat", "Dhaka", "Python"]
# sort the list
strList.sort(reverse=True)
print(strList)
print(data)
print(type(data))

# list access
print("print 0 indexed value:",data[0])
print("print 1:4 indexed value:", data[1:4])

# list  addd 
data.insert(3, "Bangladesh")
data.append("Java")
tuple = ("Laravel","Django")
data.extend(["C", "C++"])
data.extend(tuple)

# list value change
data[1] = 27
data[6] = "PHP"

# list remove
data.remove("C")
data.pop()
del data[-2]

# show data
print(data)