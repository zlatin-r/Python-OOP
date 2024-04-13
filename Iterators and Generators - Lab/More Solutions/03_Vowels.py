class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.vowels_in_string = [v for v in self.string if v.lower() in self.vowels]

    def __iter__(self):
        return iter(self.vowels_in_string)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
