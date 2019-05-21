class MyList():
    def __init__(self, iterable):
        self.lst = list(iterable)
        self._max = max(self.lst)
        self._min = min(self.lst)

    # always return 100, just for demonstrational purposes
    def __len__(self):
        return len(self.lst)

    # provide an interface for our list
    def append(self, item):
        if item < self._min:
            self._min = item
        if item > self._max:
            self._max = item
        self.lst.append(item)

    def __repr__(self):
        return str(self.lst)

    def __getitem__(self, index):
        return self.lst[index]


a = MyList((1,2,3,5,10))
# a.insert(3, 4) # this doesn't work any more.
a.append(100)
print(a[3])
print(a)
