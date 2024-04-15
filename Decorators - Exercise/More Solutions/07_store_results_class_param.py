class store_results():
    _DIR = "files"

    def __init__(self, file_name: str):
        self._file_name = file_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(f"{self._DIR}/{self._file_name}", "a") as file:
                file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")

        return wrapper


@store_results("log.txt")
def add(a, b):
    return a + b


@store_results("log.txt")
def mult(a, b):
    return a * b


add(2, 22)
mult(26, 4)
