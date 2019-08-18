from multiprocessing import Pool
from math import sqrt
import time



start_time = time.time()
l = list(range(3000000))

with Pool() as p:
    result = p.map(is_prime, l)
print("took: ", time.time()-start_time)
