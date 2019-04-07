lst = [[1,2,3], [4,5,6], [7,8,9]]

#double for loop
for row in lst:
    for c in row:
        print(c, end=' ')
    print()

#triple?
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            print(i, j, k)
