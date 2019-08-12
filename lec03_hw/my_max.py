def my_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        x, *y = lst
        return max(x, my_max(y))
