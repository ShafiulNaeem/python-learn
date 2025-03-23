import json

try:
    file = open("writeData.json", "x")
    data = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "email": "teast@ehwe",
        "isStudent": True,
        "isTeacher": False,
        "isEmployed": True,
        "isUnemployed": False,
        "languages": ["English", "Spanish", "French"],
        "hobbies": ["Reading", "Swimming", "Running"],
        "tuple": (1, 2, 3),
        "dyyict": [
            {"name": "John", "age": 30},
            {"name": "John", "age": 30}
        ]
    }
    json_data = json.dumps(data, indent=4)
    # file.write(json_data)
except FileNotFoundError as e:
    print("Error", e)
finally:
    file.close()
