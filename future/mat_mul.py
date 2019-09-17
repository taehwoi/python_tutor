from random import randint
from multiprocessing import Pool
import numpy as np
import time


# change DEBUG to True to see matrices printed
# Print them when the SIZE is a small number ( < 4?)
DEBUG = False
SIZE = 500
a = [[randint(-100,100) for _ in range(SIZE)] for _ in range(SIZE)]
b = [[randint(-100,100) for _ in range(SIZE)] for _ in range(SIZE)]
npa = np.array(a)
npb = np.array(b)
# a = [[1,2],[3,4]]
# b = [[1,2],[3,4]]

# the single core implementation
def matrix_multiplication(m0, m1):
    """The following algorithm is exactly how suhak's jungsuk does matrix
    multiplication"""

    # build resulting matrix
    res = [[0 for x in range(len(m0))] for x in range(len(m1))]

    # iterate column of lefthand
    for k in range(len(m0[0])):
    # iterate row of lefthand
        for i in range(len(m0)):
            # r = ith row, kth column
            r = m0[i][k]
            for j in range(len(m1)):
                # ith row, jth column of result is summing
                # r * kth row, jth column of righthand
                res[i][j] += (r * m1[k][j])
    return res

def transpose(m):
    # zip(*m) returns the transposed list, but its elements changed to tuples.
    # therefore we change its type to list.
    return [list(r) for r in zip(*m)]

def f(column):

    # functions used in pool can only accept ONE arguments.
    # Therefore, instead of f(m0, c), we use global a to access the lefthand
    # matrix
    global a

    # build resulting column
    res = [0 for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            res[i] += (a[i][j] * column[j])
    return res

if DEBUG:
    for (r, r2) in zip(a, b):
        print(r,"  ", r2)
"""SINGLECORE"""

# get the time before the operation
start = time.time()

result = matrix_multiplication(a, b)

# get the time after the operation
end = time.time()

# the difference between the two becomes the time spent
print("singlecore took: ", end - start)

"""MULTICORE"""

start = time.time()
# initiate a pool
with Pool() as p:
    # transpose the righthand matrix so that we can do column-wise access
    ll = transpose(b)

    if DEBUG:
        print("RIGHT matrix transposed:")
        for l in ll:
            print(l)

    # apply f to elements in l, using parallelization
    # the result would be list of list(columns).
    # We can transpose it back to match the row-wise representation
    tmp = p.map(f, ll)

    # transpose back to get the correct result
    ret = transpose(tmp)

    if DEBUG:
        print("result of singlecore:")
        for r in result:
            print(r)
        print("result of multicore:")
        for r in ret:
            print(r)

    end = time.time()
print("multicore took: ", end - start)

start = time.time()
r = np.dot(npa, npb)
end = time.time()
print("numpy took: ", end - start)
# check that multicore version works correctly
assert(result == ret)
assert(np.array_equal(np.array(result), r))
