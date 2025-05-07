from pathlib import Path

path = Path("output.txt")
path.write_text("hello")
print("Wrote to output.txt")
