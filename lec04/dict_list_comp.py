import timeit
import random

l = [0] * 10000
d = {}
for i in range(10000):
    d[i] = 0

def f():
    return l[random.randint(0, len(l)-1)]
def g():
    return d[random.randint(0, len(d)-1)]

if __name__ == '__main__':
    # repeat f and g 40000 times each
    print(timeit.timeit("f()", setup="from __main__ import f",number=1000000))
    print(timeit.timeit("g()", setup="from __main__ import g",number=1000000))
