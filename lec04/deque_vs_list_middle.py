# only load deque from collections
from collections import deque
import time

l = list()
q = deque() # an empty deque

start = time.time()
for i in range(100000):
    #insert in the middle
    l.insert(len(l)//2 , i)
end = time.time()
print("list took: ", end-start)

start = time.time()
q = deque() # an empty deque
for i in range(100000):
    #insert in the middle
    q.insert(len(q)//2, i)
end = time.time()
print("deque took: ", end-start)
