def make_doubler():
    return lambda x: x * 2

doubler = make_doubler()
print("Doubler of 10:", doubler(10))  # Output: 20
