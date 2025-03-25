# heap queue : work with list
# access min and max element 
# work as binary tree 

print("== heap queue==")

import heapq

listData = [20,10,15,30,5]
heapq.heapify(listData)
print("heap queue:",listData)
# push element 
heapq.heappush(listData, 2)
print("heap queue after push:",listData)
# pop element
print("pop element:",heapq.heappop(listData))
print("heap queue after pop:",listData)
# pushpop
print("pushpop:",heapq.heappushpop(listData, 25))
print("heap queue after pushpop:",listData)
# replace 
print("replace:",heapq.heapreplace(listData, 40))
print("heap queue after replace:",listData)
# merge
listData2 = [50,60,70]
heapq.heapify(listData2)
print("merge:",list(heapq.merge(listData,listData2)))
print("listData:",listData)
print("listData2:",listData2)
# n largest
print("n largest:",heapq.nlargest(3,listData))
# n smallest
print("n smallest:",heapq.nsmallest(3,listData))



