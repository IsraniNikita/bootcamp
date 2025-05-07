from pathlib import Path

file = Path("output.txt")

if file.exists() and file.is_file():
    print(f"{file} exists and is a file.")
else:
    print(f"{file} does not exist or is not a file.")
