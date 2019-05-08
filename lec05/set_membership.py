import timeit
import random

l = list(range(10000))
s = set(l)

def f():
    return random.randint(-10000, 10000) in l
def g():
    return random.randint(-10000, 10000) in s

if __name__ == '__main__':
    # repeat f and g 40000 times each
    print(timeit.timeit("f()", setup="from __main__ import f",number=40000))
    print(timeit.timeit("g()", setup="from __main__ import g",number=40000))
