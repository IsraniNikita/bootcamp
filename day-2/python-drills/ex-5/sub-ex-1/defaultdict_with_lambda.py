from collections import defaultdict

default = defaultdict(lambda: "N/A")
default["name"] = "Alice"

print("name:", default["name"])
print("age:", default["age"])  # Key doesn't exist
