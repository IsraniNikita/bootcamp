import os

filename = "temp.txt"

# LBYL style - race condition risk between exists check and open
if os.path.exists(filename):
    with open(filename) as f:
        print(f.read())
else:
    print("File does not exist")
