"""NUMBERS NUMBERS NUMBERS"""
a, b, c = input().split()
# There are easier ways to handle this,
# but I will only use what we've learned in lecture 01.
a = int(a)
b = int(b)
c = int(c)

nums = [a,b,c]

print("{} {:0.2f}".format(sorted(nums)[len(nums)//2], sum(nums)/len(nums)))
