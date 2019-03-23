# now we start combining them
# we call these 'iterables'
# personally, I believe python is very strong in working with lists
# so lets get used to them

a = (1, 2)
b = [1, 2, 3]
c = [55, -1, 934, 123012, -10034]
print(a)
print(b)
print(a[0], a[1])
print(sum(c))
# pretty deep topic, but lets just keep it at this level
print(sorted(c))
# print(a+b) error
# print(a[2]) <- error
print(a + (1, 2))
print(b+[1])
print(b+b) # this works the way you think it should
print(b*3) # this works the way you think it should

# we can change a list, but not a tuple.  b[1] = 'acv' # notice how it does not have to be an int.  a[1] = 'acv' # error 



# print an iterable without the brackets
# 1) lets use this for the time being
print(*a)
# 2) these seems more complicated, but will come in handy later on
# print(' '.join(map(str, a)))

# len is also used for iterables
# in a way, string is also an iterable
print(len(b))
# check for membership. Not super efficient,
# will learn a better way later on.
print(1 in b)
print(4 in b)

# tuples are memory efficient compared to lists,
# but lets focus on lists

#listfying stuffs(that are iterable)
# print(list(3)) int 3 is not iterable
a = list('thequickbrownfoxjumpsoverthelazydog')
print(a)

# gettings parts of the lists(or an iterable)
a = 'abcabcabcabcabc'
print(a, len(a))
print(a[1:], len(a[1:]))
print(a[1:3], len(a[1:3])) # notice how 3 is excluded
print(a[::-1]) #reverse
print(a[::2]) # every 2's
print(a[::3]) # every 3's
print(a[1::3]) # every 3's, starting from 1

# some applications

# is str a palindrome?
a = 'palindromeemordnilap'
print(a == a[::-1])


# how do we build a list from 1 to 100?
# a = [1,2,3,.........] forever?

# 1)
# just like subscription, last element is excluded
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
# this line of code almost froze my laptop
# print(3294802384 in list(range(1, 999999999)))
# we will talk about code efficieny throughout the course


# before we move on, lets input() stuffs
# we will deal with functions later on, 
# but lets get used to input()
name = input('type in your name\n')
age = input('your age\n')

print("I am " + name)
# notice the conversions
# int by itself, can be printed,
# but to concatanate with a string, it HAS to be converted to a string
# but there is better way that we will learn later on.
# or just Google it! It's just that easy
print("I was " + str(int(age)-1) + " last year" )
# what would this do?
print(list(range(1, input())))
