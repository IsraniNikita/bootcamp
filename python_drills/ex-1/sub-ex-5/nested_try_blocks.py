try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner: ValueError caught")
        raise
except Exception as e:
    print("Outer: Exception caught -", e)
