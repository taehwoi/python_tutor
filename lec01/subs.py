# gettings parts of the lists(or an iterable)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst[start:stop:step]
print(lst, len(lst))
print(lst[1:], len(lst[1:]))
print(lst[1:3], len(lst[1:3])) # notice how 3rd item is excluded
print(lst[::-1]) #reverse
print(lst[::2]) # every 2's
print(lst[::3]) # every 3's
print(lst[1:7+1:3])
