from Shape import Shape
class Circle(Shape):
    radius = 10
    @classmethod
    def set_radius(self, radius):
        self.radius = radius
    @property
    def get_radius(self):
        return self.radius
    @get_radius.setter
    def get_radius(self, value):
        self.radius = value

    @Shape.logger
    def area(self):
        super().log("This is a log message from Circle")
        return 3.14 * self.radius * self.radius