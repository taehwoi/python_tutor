x = [1,2,3]
def change_io():
    print("Input/Output state changed")

def change_element_of_list(l):
    l[0] = 3
change_element_of_list(x)
print(x)

x = 3
def change_4(y):
    y = 4
change_4(x)
print('x is now:', x)

def change(x):
    print('x:', x)
    x = [4,5,6]
    print("x changed:", x)
change(x)
print('x is now:', x)
