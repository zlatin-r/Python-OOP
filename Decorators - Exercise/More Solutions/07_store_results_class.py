class store_results:
    _FILE = "files/log.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(self._FILE, "a") as file:
            file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(12, 2)
mult(6, 14)
