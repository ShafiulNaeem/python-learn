from Log import Log
class Main:
    def __init__(self, filename):
        self.logDta = Log(filename)
    
    @Log.logger
    def test(self,oid):
        self.logDta.log("Test")
        return "Man is a social animal"

# Create an object of Log class

data = Main("oop/main.log")
print(data.test(4))
print(data.logDta.read())
# print(data.read())
# print(data.log("This is a log message"))
    
