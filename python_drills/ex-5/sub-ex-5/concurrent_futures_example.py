from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor() as executor:
    results = executor.map(square, range(5))
    print(list(results))
