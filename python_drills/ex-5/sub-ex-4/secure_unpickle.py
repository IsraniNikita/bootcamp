import json

data = {"name": "Nikita", "age": 20}
json_str = json.dumps(data)
print("Safe serialization using JSON:", json_str)

import marshal
code = marshal.dumps(data)
print("Unsafe but fast (marshal) serialized:", code)
