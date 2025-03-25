from collections import Counter
# Counter is a dictionary subclass which helps count hashable objects
# It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values
# Counts are allowed to be any integer value including zero or negative counts

val = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
c = Counter(val)
c.update([1,3,7])
print("counters:",c)
# print only items
print(list(c.elements()))
# most common pair
print("most common:",c.most_common(4))
# subtract
c.subtract([1,2,3,7,7])
print("subtract:",c)
# intersection
d = Counter([1,2,3,4,5])
print("intersection:",c & d)
# union
print("union:",c | d)
# clear
c.clear()
