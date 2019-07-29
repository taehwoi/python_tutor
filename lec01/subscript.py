tup = (1, 'ab', 3) # tuple
lst = [1, 2, 'ab'] # list
nums = [55, -1, 934, 123012, -10034]
s = 'StringIsalsoIteRaBLe'

print(nums[0])
print(s[-1])
print(s[-2])

nums[1] = 100
print(nums[1])
# s[-1] = 'c', tup[1] = 'abc'??

#unpacking
x, y, z = lst # len(lst) == 3
print(x, y, z)
x, *y = s # len(s) != 2
print(x, y)
