print("=== tuple start ===")
data = ("Python", "Java", "C#", "JavaScript", "Ruby", "PHP", "Laravel", "Django")
print(data)
print(type(data))
# tuple access
print("=== tuple access ===")
print("print 0 indexed value:",data[0])
print("print 1:4 indexed value:", data[1:4])
# tuple update
print("=== tuple update ===")
updateData = list(data)
updateData[2] = "C++"
updateData = tuple(updateData)
# ff = ("ff")
updateData = updateData[:] + ("ww",)
updateData = updateData[:5] + ("ff", "kk",) + ("gg",) + ("hh",) + ("jj",)
print(updateData)

# tuple unpacking
print("=== tuple unpacking ===")
a, b, c, d, e, f, g, h = data
print(a, b, c, d, e, f, g, h)
f,g,*h = updateData
print(f,g,h)
