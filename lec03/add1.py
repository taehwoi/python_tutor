def doubles(l):
    if not l:
        return []
    else:
        return [l[0]*2] + doubles(l[1:])

print(doubles([1,2,3]))
