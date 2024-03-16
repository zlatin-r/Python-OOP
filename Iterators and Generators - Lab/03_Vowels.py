class vowels:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.vowels = ["a", "e", "i", "o", "u", "y"]
        self.index = -1
        self.vowels_values = [c for c in self.iter_obj if c.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
