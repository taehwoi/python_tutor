tup = (1, 'ab', 3) # tuple
lst = [1, 2, 'ab'] # list
nums = [55, -1, 934, 123012, -10034]
s = 'StringIsalsoIteRaBLe'

print(tup)
print(lst)
print(sum(nums))
print(max(nums))
print(sorted(nums)) # new list
print(sorted(s))
nums.sorted() # changes nums itself
print(nums)
# why not tup.sorted()?
print(len(s))
print(list(s))

# pretty intuitive
print(lst + lst)
print(lst + [4])
print(s + 'abc')
print(s * 3)
lst.append(4)
print(lst)
