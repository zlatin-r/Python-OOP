class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.number == 0:
            raise StopIteration

        self.number -= 1

        if self.index > len(self.sequence) - 1:
            self.index = 0

        return self.sequence[self.index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
