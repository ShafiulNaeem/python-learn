import json
try:
    file = open("text.json", "r")
    data = json.load(file)
    print(data)
except FileNotFoundError as e:
    print("Error",e)
finally:
    file.close()