import time
import random

l = list(range(10000))
s = set(l)

start_time = time.time()
for _ in range(50000):
    random.randint(-10000, 10000) in l
end_time = time.time()
print("search in list took: ", end_time - start_time)

start_time = time.time()
for _ in range(50000):
    random.randint(-10000, 10000) in s
end_time = time.time()
print("search in set took: ", end_time - start_time)
