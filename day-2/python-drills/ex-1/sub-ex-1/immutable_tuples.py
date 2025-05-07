t = (1, 2, 3)
try:
    t[0] = 10
except TypeError as e:
    print("Error:", e)
