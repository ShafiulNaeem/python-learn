print("==== start dict ====")
person = {
    'name': 'Md. Shafiul Naeeem Rifat',
    'age': 28,
    'lang': [
        'php',
        'python'
    ]
}

print(person.update({"age":27}))

# access dict
print("==== access dict ====")
print(person['name'])
print(person.keys())
print(person.values())
items = person.items()
for i in person: 
 print("person", i, person[i],type(i),type(person[i]))
 if type(person[i]) == list:
     person[i].append("Java")
     for j in person[i]:
         print("list", j)
print(len(items))

# dict add and update
print("==== dict add and update ====")
person['city'] = 'Dhaka'
person.update({'country':'Bangladesh'})
print("after add and update:",person)

# dict remove
print("==== dict remove ====")
del person['city']
person.pop('country')
print("after remove:",person)

# dict loop and comprehension
print("==== dict loop and comprehension ====")
phpStack = {}
for i in person:
    if i == "lang":
        phpStack.update({i:person[i]})

stack = {i:person[i] for i in person if i == "lang"}
print("after loop and comprehension:",phpStack,stack)

# dict copy
print("==== dict copy ====")
copyPerson = person.copy()
copyPerson['name'] = "Rifat"
print("copy person:",copyPerson)
dict1 = dict(person)
print("dict1:",dict1)

# dict join
print("==== dict join ====")
person1 = {
    'name': 'Md. Shafiul Naeeem Rifat',
    'age': 28,
    'lang': [
        'php',
        'python'
    ]
}
person2 = {
    'city': 'Dhaka',
    'country': 'Bangladesh'
}
person1.update(person2)
print("after join:",person1)

# dict nasted 
print("==== dict nasted ====")
person3 = {
    'name': 'Md. Shafiul Naeeem Rifat',
    'age': 28,
    'lang': {
        'php': 'Laravel',
        'python': 'Django'
    }
}
print(person3['lang']['php'])

for i in person3:
    if type(person3[i]) == dict:
        for j in person3[i]:
            print(j,":", person3[i][j])


