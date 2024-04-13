class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.string):
            if self.string[self.index].lower() in self.vowels:
                return self.string[self.index]
            else:
                continue
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
