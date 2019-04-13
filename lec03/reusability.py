def mat_mul(m0, m1):
    """crude matrix multiplicaiton"""
    res = [[0 for x in range(len(m0))] for x in range(len(m1))]
    for k in range(len(m1[0])):
        for i in range(len(m0)):
            r = m0[i][k]
            for j in range(len(m1)):
                res[i][j] += (r * m1[k][j])
    return res

a = [[1,2],[3,4]]
b = [[3,2],[1,3]]
c = [[1,4],[3,5]]
d = [[3,2],[8,1]]

t = mat_mul(a,b)
k = mat_mul(c,d)
mat_mul(t, k)
