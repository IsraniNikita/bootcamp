from contextlib import suppress

with suppress(FileNotFoundError):
    with open("no_such_file.txt") as f:
        print(f.read())

print("No crash — FileNotFoundError suppressed")
