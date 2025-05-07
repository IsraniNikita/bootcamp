from pathlib import Path

path = Path("sample.txt")
if path.exists():
    content = path.read_text()
    print("File content:", content)
else:
    print("sample.txt not found.")
