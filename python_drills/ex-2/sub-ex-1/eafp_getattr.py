class Dummy:
    name = "Bot"

obj = Dummy()

print(getattr(obj, "age", "Attribute not found"))
