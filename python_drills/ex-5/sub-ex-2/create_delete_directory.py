import os
import shutil
import tempfile

temp_dir = tempfile.mkdtemp()
print("Created directory:", temp_dir)

# Do something inside it
file_path = os.path.join(temp_dir, "example.txt")
with open(file_path, "w") as f:
    f.write("temporary content")

print("File created:", file_path)

# Cleanup
shutil.rmtree(temp_dir)
print("Temporary directory deleted.")
