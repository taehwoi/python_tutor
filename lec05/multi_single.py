from multiprocessing import Pool
import time

def is_prime(n):
    if n & 1 == 0:
        return True
    d = 3
    while d * d <= n:
        if n % d == 0:
            return True
        d = d + 2
    return False

l = list(range(2000000))

start_time = time.time()
result = [is_prime(n) for n in l]
end_time = time.time()
print("single took: ", end_time-start_time)

start_time = time.time()
with Pool() as p:
    result = p.map(is_prime, l)
end_time = time.time()

print("multi took: ", end_time-start_time)
