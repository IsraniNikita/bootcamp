def uppercase(value):
    if isinstance(value, str):
        return value.upper()
    else:
        return "Invalid input type"

print(uppercase("hello"))
print(uppercase(123))
