funcs = [abs, str, hex]

print("Apply each to -42:")
for f in funcs:
    print(f.__name__, "->", f(-42))
