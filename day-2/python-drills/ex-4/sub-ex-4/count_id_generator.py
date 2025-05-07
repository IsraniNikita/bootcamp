from itertools import count

id_gen = count(1)
for _ in range(5):
    print(f"Generated ID: {next(id_gen)}")
