import multiprocessing
import time

class Shape:

    data = []
    
    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def calculate(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print(f"Area of rectangle with length {self.length} and breadth {self.breadth} is {self.area()}")
        time.sleep(2)
        print(f"Perimeter of rectangle with length {self.length} and breadth {self.breadth} is {self.perimeter()}")

    @staticmethod
    def test(data):
        for index,value in enumerate(range(1, 6)):
            print(f"index: {index} value: {value}")
            data[index] = value
    
    @staticmethod
    def square(qeue):
        for index,value in enumerate(range(1, 6)):
            print(f"index: {index} value: {value}")
            qeue.put(value*value)



if __name__ == "__main__":
    s = Shape()
    p1 = multiprocessing.Process(target=s.calculate, args=(10,20))
    p2 = multiprocessing.Process(target=s.calculate, args=(20,30))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # share data betwen processes
    dta = multiprocessing.Array('i', 5)
    p3 = multiprocessing.Process(target=s.test, args=(dta,))
    p3.start()
    p3.join()
    print("Done")
    print("Data:",dta[:])

    # multiprocessing Queue
    print("===Queue Example===")
    qeue = multiprocessing.Queue()
    p4 = multiprocessing.Process(target=s.square, args=(qeue,))
    p4.start()
    p4.join()

    while not qeue.empty():
        print(qeue.get())


