class Runnable:
    """
        Creates chainable instance of a function
    """
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        def chained_func(*args, **kwargs):
            return other(self.func(*args, **kwargs))

        return Runnable(chained_func)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def add_five(x):
    return x + 5


def multiply_by_two(x):
    return x * 2


if __name__ == "__main__":
    runnable_func1 = Runnable(add_five)
    runnable_func2 = Runnable(multiply_by_two)
    chain = runnable_func1 | runnable_func2
    result = chain(4)
    print(result)
