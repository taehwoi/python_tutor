print("Hello World!")


x = 7
bigx = 9999999999999128340928349182349028144
y = 0.1
s = 'abc'
c = 'c'
b = True
print(type(x)) # int(eger)
print(type(bigx)) # also int...
print(type(y)) # float
print(type(s)) # str(ing)
print(type(c)) # also str...
print(type(b)) # bool(ean)

print("possible operations for int")
print(x + x)
print(x * 2)
print(x ** 2)
print(bigx ** 2) # not so easy in C
print(x/4) # not accurate
print(x // 3) # int
print(bigx % x) # int
print(x == x) # notice the '=='
print(x != x)
print(x > y)

print(len('abc')) # length of 'abc'
print('abc' + 'abc') # 'abcabc'
print('abc' * 3) # guess
print('abc' == 'abc')
print('abc' != 'cba')
print(type('123'))
print(type(int('123'))) # guess
print('abc'.upper()) # 'ABC'
print('g' in 'abcdef') # guess the meaning

print(not True)
print(True and False)
print(True or False)
print(True==1)
print(True==-1)
print(True==2)
print(True==0) # True == 1 only
print(False==0)
print(False==-1)
print(False==3) # False == 0 only
print(True + 2) # notice True -> 1
print(False * 99) # notice False -> 0
