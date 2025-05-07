from functools import partial

# Fixing base to 2 for int conversion
base2 = partial(int, base=2)

print(base2('1011'))  # Output: 11
