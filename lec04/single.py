from math import sqrt
import time


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


start_time = time.time()

l = list(range(3000000))
result = [is_prime(n) for n in l]

print("took: ", time.time()-start_time)
