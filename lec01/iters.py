tup = (1, 'ab', 3) # tuple
lst = [1, 2, 'ab'] # list
nums = [55, -1, 934, 123012, -10034]

print(tup)
print(lst)
print(lst[0], lst[2]) # start from 0.
lst[2] = 3
# tup[2] = 3 why not?

print(sum(nums))
print(max(nums))
print(sorted(nums)) # new list
print(nums)
nums.sorted() # on nums it self
print(nums)
print(len(nums))

s = 'IamAlsoanIterable'
print(len(s))
print(list(s))
print(sorted(s))
# sorted(tup) why not?

# pretty intuitive
print(lst + lst)
print(lst * 3)
lst.append(4)
print(lst)
