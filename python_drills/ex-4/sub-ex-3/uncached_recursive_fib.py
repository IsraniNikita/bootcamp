def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Performance comparison
print(fib(30))  # Output: 832040
