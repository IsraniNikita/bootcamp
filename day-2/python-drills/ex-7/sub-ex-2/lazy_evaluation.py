import sys
import itertools

# 1. Generator to read large file line by line (simulation)
def line_generator():
    for i in range(1_000_000):
        yield f"Line {i}"

# 2. Generator vs List memory usage
gen = (x * x for x in range(1000000))
lst = [x * x for x in range(1000000)]
print("Generator size:", sys.getsizeof(gen))
print("List size:", sys.getsizeof(lst))

# 3. Lazy CSV Filter
def csv_filter(data):
    for row in data:
        if "error" in row:
            yield row

data_stream = ["ok", "error: something", "ok", "error: again"]
for row in csv_filter(data_stream):
    print("Filtered row:", row)

# 4. Short-circuiting with any()
big_list = list(range(1, 10_000_000))
has_99_multiple = any(x % 99 == 0 for x in big_list)
print("Any multiple of 99 found:", has_99_multiple)

# 5. itertools.islice example
first_10_lines = itertools.islice(line_generator(), 10)
print("First 10 lines from generator:")
for line in first_10_lines:
    print(line)

# 6. Avoid temporary lists
total = sum(x for x in range(1000000))
print("Total sum without temporary list:", total)

# 7. Streaming file copy (simulated)
def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        for line in src:
            dest.write(line)

# 8. Yield vs Return
def even_numbers(max_val):
    for i in range(max_val):
        if i % 2 == 0:
            yield i

evens = even_numbers(20)
print("Even numbers using yield:")
for e in evens:
    print(e)
