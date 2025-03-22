class Numbers:
    def __init__(self, max):
        self.max = max
        
    def __iter__(self):
        self.a = self.max
        return self
    def __next__(self):
        if self.a <= self.max and self.a >= 0:
            x = self.a
            self.a -= 1
            return x
        else:
            raise StopIteration
        
# input from user
max  = int(input("Enter the number: "))
data = Numbers(max)
data1 = iter(data)
for i in data1:
    print(i)
