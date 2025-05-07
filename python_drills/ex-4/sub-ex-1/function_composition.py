def compose(f, g):
    return lambda x: f(g(x))

add1 = lambda x: x + 1
times2 = lambda x: x * 2

composed = compose(add1, times2)
print("Compose add1(times2(3)):", composed(3))  # Output: 7
