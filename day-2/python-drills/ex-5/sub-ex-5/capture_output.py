import subprocess

result = subprocess.run(["cmd", "/c", "echo Hello"], capture_output=True, text=True)
print("Captured:", result.stdout.strip())
