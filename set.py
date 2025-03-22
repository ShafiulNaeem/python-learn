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
