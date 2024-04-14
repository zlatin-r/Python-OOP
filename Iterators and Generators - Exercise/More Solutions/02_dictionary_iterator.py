class dictionary_iter:
    def __init__(self, obj: dict):
        self.items = list(obj.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1

        res = self.items[self.index]

        return res


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
