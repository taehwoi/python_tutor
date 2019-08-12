DEFAULT = -1
tbl = [DEFAULT] * 1000

# tbl[0] = fib(0) = 0, tbl[1] = fib(1) = 1
tbl[0] = 0
tbl[1] = 1

def fibonacci(n):
    # if tbl[n] has been updated
    # use that value instead calculating
    if tbl[n] != DEFAULT:
        return tbl[n]
    # fib(n) = fib(n-1) + fib(n-2)
    else:
        # update the table
        tbl[n] = fibonacci(n-1) + fibonacci(n-2)
        return tbl[n]

print(fibonacci(100))
