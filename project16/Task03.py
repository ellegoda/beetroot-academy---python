class CustomIterable:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.values):
            result = self.values[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.values[key]


my_iterable = CustomIterable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


for value in my_iterable:
    print(value)


print(my_iterable[0])
print(my_iterable[9])