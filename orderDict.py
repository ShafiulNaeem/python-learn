print("=== order dict ===")
# subclass of dict and difference is key order 

from collections import OrderedDict

dictData = OrderedDict();
dictData['a'] = 1
dictData['b'] = 2
dictData['c'] = 3
print("OrderedDict:",dictData)

ordeDictData = OrderedDict();
ordeDictData['b'] = 2
ordeDictData['c'] = 3
ordeDictData['a'] = 1
print("OrderedDict:",ordeDictData)

# compare
print("compare order:",dictData == ordeDictData)
# reverse order dict
print("reversed:",list(reversed(ordeDictData.items())))
# pop item
print("pop item first:", ordeDictData.popitem(last=False))
print("OrderedDict:",ordeDictData)
# insertion and delete
ordeDictData["b"] = 2
ordeDictData["d"] = 4
ordeDictData["e"] = 5

ordeDictData.pop('b')

ordeDictData.move_to_end('a',last=False)
ordeDictData.update([('e',10)])
print("OrderedDict:",ordeDictData)



