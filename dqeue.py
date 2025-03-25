# description: its stand for double ended queue,,
# its add and remove element from both end
# its work FIFO and LIFO 
from collections import deque
# create deque
data = deque([1,2,3,4,5,6,7,8,9,10])
print("deque:",data)

# append element from right
data.append(11)
print("append right:",data)
# append element from left
data.appendleft(12)
print("append left:",data)
# pop element from right
print("pop right:",data.pop())
print("deque:",data)
# pop element from left
print("pop left:",data.popleft())
print("deque:",data)
# remove element
data.remove(5)
print("remove:",data)
# reverse deque
data.reverse()
print("reverse:",data)
# clear deque
data.clear()
print("clear:",data)
# extend deque
data.extend([1,2,3,4,5,6,7,8,9,10])
print("extend:",data)
# extendleft deque
data.extendleft([11,12,13,14,15])
print("extend left:",data)
# rotate deque
data.rotate(2)
print("rotate:",data)
data.rotate(-2)
print("rotate:",data)
# count element
print("count:",data.count(1))
# index element
print("index:",data.index(1))
# insert element
data.insert(2,100)
print("insert:",data)
# maxlen
data = deque([1,2,3,4,5,6,7,8,9,10],maxlen=5)
print("maxlen:",data)
data.append(11)

