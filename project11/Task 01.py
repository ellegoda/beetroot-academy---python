def logger(func):
    func_name = func.__name__

    def inner_logger(*args):
        args_str = ", ".join([repr(arg) for arg in args])
        print(func_name, "called with", args_str)

        result = func(*args)
        return result

    return inner_logger


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(4, 5)