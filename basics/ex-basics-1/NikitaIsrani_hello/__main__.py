import sys
from . import say_hello  # Import say_hello from the current package

def main():
    if len(sys.argv) > 1:
        say_hello(sys.argv[1])  # If an argument is passed, use it
    else:
        say_hello()  # Otherwise, greet with "World"

