lst = [n for n in range(10)]
lst == list(range(10))

# 1
# 2
# 3
input_nums = [int(input()) for _ in range(5)]
# convention: we use _ when we don't use it.

# 1 2 3 ....
input_nums = [int(n) for n in input().split()]

lst = [n**2 for n in range(10)]

lst = [[0] * 10 for _ in range(10)]

uppers = [c for c in 'iaMaSTring' if c.isupper()]

# try to avoid this. WHY?
lst = [print("HELLO") for _ in range(10)]
