d = {'a':1, 'b':2, 'c':3}
# dictionaries are iterable
print(len(d))

# iterate over keys
for k in d:
    print(k)

# iterate over values
for v in d.values():
    print(v)

# get the key:value pair
for k, v in d.items():
    print(k, v)
