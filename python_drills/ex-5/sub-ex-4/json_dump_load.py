import json

data = {"name": "Nikita", "age": 20}
json_str = json.dumps(data)
print("Serialized JSON:", json_str)

loaded_data = json.loads(json_str)
print("Deserialized:", loaded_data)
