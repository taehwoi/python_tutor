# only load deque from collections
from collections import deque
import time

l = []
q = deque() # an empty deque

start = time.time()
for i in range(100000):
    #insert at front
    l.insert(0, i)
end = time.time()
print("took: ", end-start)

start = time.time()
q = deque() # an empty deque
for i in range(100000):
    #insert at front
    q.appendleft(i)
end = time.time()
print("took: ", end-start)
