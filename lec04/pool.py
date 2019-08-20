from multiprocessing import Pool


def f(n):
    print(n)
    return n*n

l = [1,2,3,4,5,6,7,8]

with Pool() as p:
    # the order of execution is not guaranteed
    result = p.map(f, l)
print(result)
