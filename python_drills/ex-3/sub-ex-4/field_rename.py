from collections import namedtuple

# First field is invalid so rename=True auto-renames to _0
Data = namedtuple("Data", ["class", "value"], rename=True)
d = Data("Math", 100)
print(d)
