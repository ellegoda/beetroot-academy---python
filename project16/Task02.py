class InRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):

        if (self.step > 0 and self.current < self.end) or (self.step < 0 and self.current > self.end):
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration


my_range = InRange(1, 100, 5
                   )

for value in my_range:
    print(value)