import multiprocessing
import time

class Shape:
    
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

if __name__ == "__main__":
    s = Shape()
    p1 = multiprocessing.Process(target=s.calculate, args=(10,20))
    p2 = multiprocessing.Process(target=s.calculate, args=(20,30))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Done")


