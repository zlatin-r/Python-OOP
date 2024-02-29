class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        sorted_data = sorted(self.data, reverse=True)
        result = ", ".join(sorted_data)
        return f"[{result}]"
