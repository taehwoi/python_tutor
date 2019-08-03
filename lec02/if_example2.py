ERROR_MSG = "lst is empty"

#'ask for permission' pattern
if len(lst) != 0:
    print(lst[0])
else:
    print(ERROR_MSG)

if lst:
    print(lst[0])
else:
    print(ERROR_MSG)
