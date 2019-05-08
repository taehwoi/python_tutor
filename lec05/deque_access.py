from collections import deque
import random
import timeit

l = list(range(1000000))
q = deque(range(1000000))

def f():
    return l[random.randint(0,999999)]
def g():
    return q[random.randint(0,999999)]

if __name__ == '__main__':
    # repeat f and g 40000 times each
    print(timeit.timeit("f()", setup="from __main__ import f",number=100000))
    print(timeit.timeit("g()", setup="from __main__ import g",number=100000))
