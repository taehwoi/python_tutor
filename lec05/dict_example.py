avengers = {} # use curly braces to create a dictionary

# the names are the keys, and the hero identity are values
avengers['brucebanner'] = 'hulk'
avengers['tonystark'] = 'ironman'
avengers['peterparker'] = 'spiderman'
avengers['steverogers'] = 'captainamerica'

print(avengers['tonystark'])
# overwrite key's value
avengers['steverogers'] = 'blueskull'

# no key: error
# print(avengers['thanos'])
