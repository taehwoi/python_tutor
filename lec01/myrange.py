print(list(range(1, 100 + 1)))
print(list(range(2, 100 + 1, 2)))

sum(range(100+1))
print(*list(range(0, 100+1, 5)))

# why is this possible?
3234294802384 in range(1, 99999999999999999999999999999999999)
# when this is not?
3234294802384 in list(range(1, 999999999))
