def fibonacci(n):
    # fib(0) = 0, fib(1) = 1
    if n == 0 or n == 1:
        return n
    # fib(n) = fib(n-1) + fib(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
