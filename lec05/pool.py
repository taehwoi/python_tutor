from multiprocessing import Pool


def f(n):
    return n*n

l = [1,2,3,4,5,6,7,8]

with Pool() as p:
    result = p.map(f, l)

print(result)
