d = {} # use curly braces to create a dictionary

# the name becomes the key, and the hero identity becomes value
d['brucebanner'] = 'hulk'
d['tonystark'] = 'ironman'
d['peterparker'] = 'spiderman'
d['steverogers'] = 'captainamerica'

print(d['tonystark'])
# overwrite key's value
d['steverogers'] = 'blueskull'
# no key: error
# print(d['thanos'])
