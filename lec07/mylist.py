class MyList(list):
    """a list that keeps track of max and min"""
    def __init__(self, iterable):
        super().__init__(iterable)
        self._max = max(iterable)
        self._min = min(iterable)

    # always return 100, just for demonstrational purposes
    def __len__(self):
        return 100

    def append(self, item):
        if item < self._min:
            self._min = item
        if item > self._max:
            self._max = item
        super().append(item)


a = MyList((1,2,3,5,10))
a.insert(3, 4)
a.append(100)
print(a[3:4])
print(a)
print(a._max)
# overriden by the child
print(len(a))
