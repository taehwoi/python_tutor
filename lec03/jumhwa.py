def a(n):
    # Base Case:
    if n == 1:
        # a(1) = 3
        return 3
    else:
        # a(n) = a(n-1) + 2
        return a(n-1) + 2
