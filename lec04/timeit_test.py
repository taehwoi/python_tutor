import timeit

def f():
    x = 1
    for i in range(100):
        x *= i
    return x

if __name__ == '__main__':
    print(timeit.timeit("f()", setup="from __main__ import f",number=1000000))
