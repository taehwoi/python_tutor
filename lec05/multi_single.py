from multiprocessing import Pool
from math import sqrt
import time


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

l = list(range(1000000))

start_time = time.time()
result = [is_prime(n) for n in l]
end_time = time.time()
print("single took: ", end_time-start_time)

start_time = time.time()

with Pool() as p:
    result = p.map(is_prime, l)
# with keyword handles initalization and cleanup of certain operations
# equivalent to

# p = Pool()
# do something
# p.close()
# p.join()

end_time = time.time()

print("multi took: ", end_time-start_time)
