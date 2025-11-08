from functools import wraps


"""
Decorators run in order of their stacking, 
@decorator_1
@decorator_2
def test_fn():

Here, decorator 1 will run first, then decorator 2 and then the function,
the bottom of a decorator is the inputs to it, for decorator 1, the input is the test_fn decorated by decorator2,
for decorator2 the input is the test_fn

Output is:
---------------------------------------
Decorator 1 ran
Decorator 2 ran
running function
---------------------------------------

"""


def decorator_1(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        print("Decorator 1 ran")

        return fn(*args, **kwargs)

    return inner


def decorator_2(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print("Decorator 2 ran")

        return fn(*args, **kwargs)

    return inner

@decorator_1
@decorator_2
def test_fn():
    print("running function")


if __name__ == "__main__":
    test_fn()