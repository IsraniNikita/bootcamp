it = iter([1, 2])

try:
    print(next(it))
    print(next(it))
    print(next(it))  # Will raise StopIteration
except StopIteration:
    print("No more items.")
