import subprocess, time

proc = subprocess.Popen(["ping", "-t", "127.0.0.1"], stdout=subprocess.DEVNULL)
print("Started subprocess. Will kill in 3 seconds...")
time.sleep(3)
proc.terminate()
print("Subprocess terminated.")
