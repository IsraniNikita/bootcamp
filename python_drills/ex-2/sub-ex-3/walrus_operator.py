
while (line := input("Type something (type 'exit' to quit): ")) != "exit":
    print("You said:", line)


lines = iter(["hello", "world", "exit"])
while (line := next(lines)) != "exit":
    print("You said:", line)
