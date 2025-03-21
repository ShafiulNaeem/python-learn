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

# loop  and list comprehension
phpStack = []
print("print for loop")
for i in data:
    print(i)
    if i == "PHP" or i == "Laravel":
        phpStack.append(i)

for i in range(len(data)):
    print(data[i])

n = 0
while n < len(data):
    print(data[n])
    n += 1

# list comprehension
personData = [i for i in data if i not in phpStack]
print("person data:", personData)
print("php stack:", phpStack)
# list copy
print("==== copy list ====")
copyData = data.copy()
copyData1 = list(data)
copyData2 = data[1:4]
copyData2[0] = 100
print(copyData1)
print(copyData2)
print(copyData)
print("==== copy list end ====")

# list join
print("==== join list ====")
joinData = data + phpStack
joinData.extend(phpStack)
joinData1 = joinData * 2
print(joinData)
print(joinData1)
print("==== join list end ====")

# show data
print(data)

