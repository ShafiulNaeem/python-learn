import json

# some JSON:

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

# convert into JSON:
json_data = json.dumps(data)

# result is a JSON string:
print(json_data)

# use intend
json_data = json.dumps(data, indent=4)
print(json_data)

# use separators and sort_keys
print(json.dumps(data, indent=4, separators=(". ", " = "), sort_keys=True))

# parse JSON:
data1 = json.loads(json_data)
print(data1)
