def echo():
    while True:
        received = yield
        print("Received:", received)

g = echo()
next(g)          # Prime the generator
g.send("Hello")  # Send data
g.send("World")
