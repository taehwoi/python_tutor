avengers = {'natasharomanof': 'blackwidow'} # use curly braces to create a dictionary

# the names are the KEYS, and the hero identity are VALUES
avengers['brucebanner'] = 'hulk'
avengers['tonystark'] = 'ironman'
avengers['peterparker'] = 'spiderman'
avengers['steverogers'] = 'captainamerica'

# asking for permission pattern
if 'tonystark' in avengers:
    print(avengers['tonystark'])

# overwrite key's value
avengers['steverogers'] = 'blueskull'
print(avengers['steverogers'])
