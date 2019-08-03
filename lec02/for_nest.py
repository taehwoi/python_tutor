matrix = [[1,2,3], [4,5,6], [7,8,9]]

#double for-loop
for row in matrix:
    # prints each column
    # print(*row)
    for e in row:
        print(e, end=' ')
    print()

#triple
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            print(i, j, k)
