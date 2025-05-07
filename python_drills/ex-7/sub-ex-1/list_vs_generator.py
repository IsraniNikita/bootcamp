import timeit

# List comprehension
list_time = timeit.timeit('[x*x for x in range(1000000)]', number=10)

# Generator expression
gen_time = timeit.timeit('(x*x for x in range(1000000))', number=10)

print(f"List time: {list_time} seconds")
print(f"Generator time: {gen_time} seconds")
