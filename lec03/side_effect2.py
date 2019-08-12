y = [5, 6, 7]
def change_by_global():
    global y
    print('y:', y)
    y = [8,9,10]

print("y changed:", y)
print('y is now:', y)

change_by_global()
print('y is now:', y)
