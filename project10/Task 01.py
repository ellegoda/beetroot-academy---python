def get_local_variables_count(func):
    local_vars = func.__code__.co_varnames
    local_vars = [var for var in local_vars if not var.startswith('__')]
    return len(local_vars)


def local_function():
    a = 10
    b = "Hello"
    c = [1, 2, 3]

    def inner_function():
        x = 5
        y = "World"

    print(get_local_variables_count(local_function))

local_function()