user = {"name": "Alice"}
# .get() method
print("Name:", user.get("name"))
print("Age (default):", user.get("age", "Unknown"))

# .setdefault()
user.setdefault("age", 25)
print("User dict after setdefault:", user)
