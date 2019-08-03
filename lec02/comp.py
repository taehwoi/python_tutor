lst = [n for n in range(10)]
lst == list(range(10)) # True

# getting input of 5 lines
# convention: we use '_' when we don't need the element (_=0,1,2,3,4)
input_nums = [int(input()) for _ in range(5)]
input_nums = [int(n) for n in input().split()]

lst = [n**2 for n in range(10)]
lst = [[0] * 10 for _ in range(10)]
upper = [c for c in 'AbcD' if c.isupper()]

# try to avoid this. We want to avoid side effects
lst = [print("HELLO") for _ in range(10)]
