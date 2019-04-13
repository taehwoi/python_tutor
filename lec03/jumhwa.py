def a(n):
    # Base Case:
    # a(1) = 3
    if n == 1:
        return 3
    # a(n) = a(n-1) + 2
    else:
        return a(n-1) + 2
