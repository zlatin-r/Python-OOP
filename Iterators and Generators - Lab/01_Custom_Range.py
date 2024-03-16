class custom_range:
    def __init__(self, start_index, end_index):
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = self.start_index - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.end_index:
            self.current_index += 1
            return self.current_index
        raise StopIteration


one_to_ten = custom_range(1, 5)
for num in one_to_ten:
    print(num)
