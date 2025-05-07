import sys

lst = [x for x in range(1000000)]
gen = (x for x in range(1000000))

print("List memory (MB):", round(sys.getsizeof(lst) / 1024 / 1024, 2))
print("Generator memory (bytes):", sys.getsizeof(gen))
