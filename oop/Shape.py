from Log import Log
class Shape(Log):
    def __init__(self):
        super().__init__("oop.log")

    @Log.logger
    def area(self):
        super().log("This is a log message")
        return None
    
# p = Shape()
# print(p.area())
