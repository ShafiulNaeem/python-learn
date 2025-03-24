from Log import Log
class Main(Log):
    def __init__(self, filename):
        super().__init__(filename)
    
    @Log.logger
    def test(self,oid,op):
        super().log("This is a log message")
        return "Man is a social animal"

# Create an object of Log class

data = Main("oop/main.log")
print(data.test(4,9))
print(data.read())
# print(data.read())
# print(data.log("This is a log message"))
    
