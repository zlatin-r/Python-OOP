class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.start_idx = len(self.iter_obj)
        self.end_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_idx > self.end_idx:
            self.start_idx -= 1
            return self.iter_obj[self.start_idx]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
