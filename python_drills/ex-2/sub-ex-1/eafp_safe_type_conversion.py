value = "abc"

try:
    num = int(value)
except ValueError:
    print("Cannot convert to int")
