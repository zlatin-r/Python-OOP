class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = - self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count:
            self.index += self.step
            return self.index
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
