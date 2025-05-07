try:
    value = int("abc")
    result = 10 / 0
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")
