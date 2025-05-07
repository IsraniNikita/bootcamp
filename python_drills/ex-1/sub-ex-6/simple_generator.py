def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(3):
    print(val)
