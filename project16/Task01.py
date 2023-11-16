class WithIndex:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            result = (self.index, self.iterable[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration


my_list = ['Apple', 'Banana', 'Cherry', 'Mango', 'Pineapple']

with_index_iterator = WithIndex(my_list, start=1)

for index, value in with_index_iterator:
    print(f"Index, {index}: {value}")
