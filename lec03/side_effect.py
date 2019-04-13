x = [1,2,3]
def change_io():
    print("state changed")

def change_element_of_list(l):
    l[0] = 3
change_element_of_list(x)
# changed
print(x)

def change_without_global(x):
    x = 2
# no change?!
print(x)
