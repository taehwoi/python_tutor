try: # try some code that can cause errors
    n = int(input())
    k = 3/n
# catch the errors and name them e
except:
    # only executed when there is error
    print("{} happened".format(e))
    k = 1
finally: # executes regardless of errors
    print(k)
