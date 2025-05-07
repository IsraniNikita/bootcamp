from rich import print
import sys

def main():
    name = "world"  # Default name
    if len(sys.argv) > 1:
        name = sys.argv[1]  # If a name is passed as argument
    print(f"[bold magenta]Hello, {name}[/bold magenta]! Welcome to the rich world.")
