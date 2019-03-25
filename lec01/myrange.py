print(list(range(1, 100 + 1)))
# notice how only the even numbers are printed
print(list(range(2, 100 + 1, 2)))

# gauss used (n) * (n+1) / 2, we use this
# notice how sum accepts iterables(that holds numbers)
print(sum(range(100+1)))

# quiz: print every 5's in 100 
# notice how we have to supply the first value to use steps
# computers are not that! smart
print(*list(range(0, 100+1, 5)))

# we will deal with this next week.
# [x*2 for x in range(30)] # fxxking powerful.

# a small surprise
print(3294802384 in range(1, 99999999999999999999999999999999999))
