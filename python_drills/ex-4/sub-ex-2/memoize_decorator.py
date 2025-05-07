def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            print("Returning cached result")
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper

@memoize
def add(a, b):
    print("Computing result...")
    return a + b

print(add(1, 2))
print(add(1, 2))  # This should return the cached result
