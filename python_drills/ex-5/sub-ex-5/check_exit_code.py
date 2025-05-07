import subprocess

proc = subprocess.run(["cmd", "/c", "exit 1"])
print("Exit code:", proc.returncode)
