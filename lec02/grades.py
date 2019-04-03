score = int(input())

# C style Boolean
if 90 <= score and score <= 100:
    print('A')
# use THIS!
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else: # when every boolean above is False
    print('F')
