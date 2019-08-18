from collections import deque
import time

l = []
q = deque() # an empty deque

def f():
    l = []
    for i in range(100000):
        #insert at beginning
        l.insert(0, i)
def g():
    q = deque() # an empty deque
    for i in range(100000):
        #insert at beginning
        q.appendleft(i)

if __name__ == '__main__':
    print(timeit.timeit("f()", setup="from __main__ import f",number=2))
    print(timeit.timeit("g()", setup="from __main__ import g",number=2))
