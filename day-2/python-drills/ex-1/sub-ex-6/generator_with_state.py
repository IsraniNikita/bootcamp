def running_total(lst):
    total = 0
    for num in lst:
        total += num
        yield total

for value in running_total([1, 2, 3, 4]):
    print(value)
