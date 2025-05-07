with open("sample.txt", "w") as f:
    f.write("Hello from context manager!")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
