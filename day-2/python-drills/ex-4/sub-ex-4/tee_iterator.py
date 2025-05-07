from itertools import tee

original = iter(range(5))
a, b = tee(original)

print("Iterator A:")
for item in a:
    print(item)

print("Iterator B:")
for item in b:
    print(item)
