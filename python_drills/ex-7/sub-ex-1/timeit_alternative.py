import timeit

# Timing sum(range(10000)) 1000 times
execution_time = timeit.timeit("sum(range(10000))", number=1000)
print(f"Execution time for sum(range(10000)) over 1000 runs: {execution_time:.6f} seconds")
