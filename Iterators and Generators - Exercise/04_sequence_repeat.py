class sequence_repeat:
    def __init__(self, sequence: str, times: int):
        self.sequence = sequence
        self.times = times
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.times:
            raise StopIteration

        char = self.sequence[self.iterations % len(self.sequence)]
        self.iterations += 1
        return char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
