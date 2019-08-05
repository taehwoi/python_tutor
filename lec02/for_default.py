for i in range(6):
    print("hello!")

nums = [1, 2, 3, 4, 5, 6]

# use len(nums) instead of 6 
# access list elements with their index
for i in range(len(nums)):
    print(nums[i])
    nums[i] += 1

# read the values
for e in nums:
    print(e)

# stop in the middle
for n in nums:
    print(n)
    if n == 2:
        print("We found 2!")
        break

# equivalent to print(sum(nums))
x = 0
for n in nums:
    x += n
print(x)
