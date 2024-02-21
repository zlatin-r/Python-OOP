n = int(input())


def print_row(size, row):
    print(" " * (size - row), "* " * row)


def print_upper_part(size):
    for row in range(size):
        print_row(size, row)


def print_lower_part(size):
    for row in range(size, 0, -1):
        print_row(size, row)


def print_rhombus():
    print_upper_part(n)
    print_lower_part(n)


print_rhombus()
