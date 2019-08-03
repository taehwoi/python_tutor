score = int(input())

if 90 <= score and score <= 100:
    print('A')
# chained comparison (a little bit slower*)
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else: # when every value above evals to False
    print('F')
