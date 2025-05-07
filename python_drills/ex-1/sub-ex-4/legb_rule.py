x = 10  # Global

def my_func():
    x = 20  # Local
    print("Inside function:", x)

my_func()
print("Outside function:", x)
