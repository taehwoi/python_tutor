a = [[1,2],[3,4]]
b = [[3,2],[1,3]]
c = [[1,4],[3,5]]
d = [[3,2],[8,1]]

res = [[0 for x in range(len(a))] for x in range(len(b))]
for k in range(len(b[0])):
    for i in range(len(a)):
        r = a[i][k]
        for j in range(len(b)):
            res[i][j] += (r * b[k][j])
res2 = [[0 for x in range(len(c))] for x in range(len(d))]
for k in range(len(d[0])):
    for i in range(len(d)):
        r = c[i][k]
        for j in range(len(d)):
            res[i][j] += (r * d[k][j])
# and once more
