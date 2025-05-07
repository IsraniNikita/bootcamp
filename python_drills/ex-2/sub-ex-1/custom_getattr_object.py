class SafeObject:
    def __getattr__(self, name):
        return f"{name} is not defined, returning default"

obj = SafeObject()
print(obj.username)  # Will trigger __getattr__
