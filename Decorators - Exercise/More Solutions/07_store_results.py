def store_results(func):
    def wrapper(*args, **kwargs):
        with open("files/log.txt", "a") as log:
            log.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
