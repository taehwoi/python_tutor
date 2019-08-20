# remove the key-value pair
del avengers['tonystark']

# asking for forgiveness pattern
try:
    print(avengers['tonystark'])
except KeyError as e:
    print("No {} in avengers!".format(e))
