# sub class of dict
# undefined no key error set default value 

from collections import defaultdict

# int 
intData = defaultdict(int)
data = [1,2,3,4,5,6,7,2,4,1]
l = {}

for x in data:
    intData[x] = intData[x]+1

print("int data:",intData)
print(intData[9])

# str 
strData = defaultdict(str)
strData["a"] = "dsjhsdjhsd"

print("str data:", strData)
print(strData["af"])

 # list
listData = defaultdict(list)
listData["jk"].append("go")
listData["jk"].append("hh")
print("list data:", listData["oo"])

