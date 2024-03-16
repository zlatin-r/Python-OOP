class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0
        self.num = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.num += self.step
        if self.index < self.count:
            self.index += 1
            return self.num
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


