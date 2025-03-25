from Shape import Shape
class Square(Shape):
    side = 10
    @classmethod
    def set_side(self, side):
        self.side = side
    @property
    def get_side(self):
        return self.side
    @get_side.setter
    def get_side(self, value):
        self.side = value

    @Shape.logger
    def area(self):
        super().log("This is a log message from Square")
        return self.side * self.side
    
data = Square()
data.set_side = 5
print(data.area())