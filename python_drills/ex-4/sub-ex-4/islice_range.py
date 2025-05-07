from itertools import islice

sliced = islice(range(10), 3, 7)
print(list(sliced))

