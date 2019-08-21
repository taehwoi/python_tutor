from random import randint
from multiprocessing import Pool
import time

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

def transposed(m):
    # zip([1,2,3], [3,4,5]) -> [(1,3), (2, 4), (3,5)]
    # just like a zipper, match elements with their corresponding pair
    # equivalent to tranpose, with lengths are equal

    # zip(*m) returns the transposed list, but its elements changed to tuples.
    # therefore we change its type to list.
    return [list(r) for r in zip(*m)]

def f(column):
    # functions used in pool can only accept ONE arguments.
    # Therefore, instead of f(m0, c)
    # we use global a to access the lefthand matrix
    global a

    # build resulting column
    result = [0 for x in range(len(a))]

    # do a matrix & column multiplication. Two nested for loops will suffice.
    # TODO

    return result

#BEGINNING OF CODE EXECUTION
#BEGINNING OF CODE EXECUTION
#BEGINNING OF CODE EXECUTION

# size of left, right hand matrices
SIZE = 300

# change DEBUG to True to print the matrices
# Print when the SIZE is a small number ( < 4?)
DEBUG = False

# Generate a SIZExSIZE matrix with random numbers
# lefthand
a = [[randint(-100,100) for _ in range(SIZE)] for _ in range(SIZE)]
# righthand
b = [[randint(-100,100) for _ in range(SIZE)] for _ in range(SIZE)]


if DEBUG:
    for (r, r2) in zip(a, b):
        print(r,"  ", r2)

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

    end = time.time()
print("multicore took: ", end - start)

"""SINGLECORE"""
# get the time before the operation
start = time.time()
result = matrix_multiplication(a, b)
# get the time after the operation
end = time.time()
# the difference between the two becomes the time spent
print("singlecore took: ", end - start)

if DEBUG:
    print("result of singlecore:")
    for r in result:
        print(r)
    print("result of multicore:")
    for r in ret:
        print(r)

# check that multicore version works correctly
assert(result == ret)
