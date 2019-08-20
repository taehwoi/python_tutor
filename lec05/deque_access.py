from collections import deque
import random
import time

l = list(range(1000000))
q = deque(range(1000000))

start = time.time()
for _ in range(100000):
    l[random.randint(0,999999)]
end = time.time()
print("took: ", end - start)

start = time.time()
for _ in range(100000):
    q[random.randint(0,999999)]
end = time.time()
print("took: ", end - start)
