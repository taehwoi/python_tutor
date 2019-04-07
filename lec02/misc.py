#works on iterables
t = (1, 2, 3)
print(t+t)
print(t+t+t)

l = [1,2,3]
print(l * 3)

s = 'abc'
print(s * 2)

#unpacking iterables
x, y, z = (1, 2, 3)
x, *y = [1, 2, 3, 4, 5]
x, y, *z = 'hiiam'
