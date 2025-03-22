print("=== set start ===")
data = {"Python", "Java", "C#", "JavaScript", "Ruby", "PHP", "Laravel", "Django"}
print(data)

# set access
print("=== set access ===")
for i in data:
    print(i)

x, y, *z = data
print(x, y, z)

# set add
print("=== set add ===")
data.add("C++")
data.update({"C", "C++"})
print(data)

# set remove
print("=== set remove ===")
deldata =  {"C#", "JavaScript", "Ruby", "PHP", "Laravel", "Django"}   
deldata.remove("JavaScript")
deldata.discard("JavaScript") 
# deldata.clear()
print(deldata)
# del deldata

# set loop and comprehension
print("=== set loop and comprehension ===")
phpStack = set()
for i in data:
    print('loop:',i)
    if i == "PHP" or i == "Laravel":
        phpStack.add(i)


otherData = {i for i in data if i not in phpStack}
print("other data:", otherData)
print("php stack:", phpStack)

# set join
print("=== set join ===")
joinData = otherData.union(phpStack)

# update
a = {1,2,3}
b = {1,2,4}
a.update(b)
print('update:',a)

# intersection
c  = a & b
print('intersection:',c)

# a.intersection_update(b)
print('intersection update:',a)

# difference
d = a - b
print('difference:',d)

# a.difference_update(b)
print('difference update:',a)

# symmetric difference
a.add(5)
b.add(6)
e = a ^ b
print('symmetric difference:',e)

print(joinData)
