import time

start_time = time.time()

# Some function or code to measure
sum(range(10000))

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
