class dictionary_iter:
    def __init__(self, obj: dict):
        self.items = list(obj.items())
        self.iters = len(obj)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.iters:
            raise StopIteration

        res = self.items[self.counter]
        self.counter += 1

        return res


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
