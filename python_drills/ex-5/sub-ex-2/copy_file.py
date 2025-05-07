import shutil
from pathlib import Path

src = Path("source.txt")
src.write_text("copy me!")

dst = Path("destination.txt")
shutil.copy(src, dst)
print(f"Copied {src} to {dst}")
