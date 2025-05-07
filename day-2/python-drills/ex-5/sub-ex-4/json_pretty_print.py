import json

data = {"name": "Nikita", "age": 20, "city": "Bhandara"}
json_str = json.dumps(data, indent=4, sort_keys=True)
print("Pretty JSON:\n", json_str)
