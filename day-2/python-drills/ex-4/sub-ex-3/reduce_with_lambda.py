from functools import reduce

# Using reduce to calculate factorial of n
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))

print(f"Factorial of {n} is {factorial}")  # Output: Factorial of 5 is 120
