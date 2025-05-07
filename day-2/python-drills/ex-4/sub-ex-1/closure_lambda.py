def multiplier(factor):
    return lambda x: x * factor

triple = multiplier(3)
print("Triple of 4:", triple(4))  # Output: 12
