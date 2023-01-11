def add(fn):
    def wrapped():
        return fn() + x
    return wrapped


def subtract(fn):
    def wrapped():
        return fn() - x
    return wrapped


def multiply(fn):
    def wrapped():
        return fn() * x
    return wrapped


def divide(fn):
    def wrapped():
        return fn() / x
    return wrapped


@add
@multiply
def example():
    return 2


x = 2
print(example())
