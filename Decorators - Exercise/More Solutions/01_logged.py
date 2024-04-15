def logged():
    def wrapper(function(*args)):
        result = function(*args)
        message = f"you called {function.__name__}({})"


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
