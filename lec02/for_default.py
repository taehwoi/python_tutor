for i in range(6):
    print("hello!")

nums = [1, 2, 3, 4, 5, 6]

# avoid magic numbers
for i in range(6):
    print(nums[i])
print()

# this lets us change nums[i]
for i in range(len(nums)):
    print(nums[i])
    # something new?
    nums[i] += 1

print()

# this lets us read the values
for e in nums:
    print(e)
print()

for n in nums:
    if n == 2:
        print("We found 2!")
        break

x = 0
for n in nums:
    x += n
print(x)
