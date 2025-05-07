try:
    x = int("not-a-number")
except ValueError as e:
    print("Logging error:", e)
    raise
