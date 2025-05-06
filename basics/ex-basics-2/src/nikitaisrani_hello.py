
from rich import print
import sys

def main():
    name = "world"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    print(f"[bold magenta]Hello, {name}[/bold magenta]! Welcome to the rich world.")
