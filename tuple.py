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
# tuple loop
print("=== tuple loop ===")
for i in data:
    print(i)

for i in range(len(data)):
    print(data[i])

n = 0
while n < len(data):
    print(data[n])
    n += 1
# tuple comprehension
print("=== tuple comprehension ===")
phpStack = []
for i in data:
    if i == "PHP" or i == "Laravel":
        phpStack.append(i)

phpStack = tuple(phpStack)
print(phpStack)

