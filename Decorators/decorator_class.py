
"""
We are essentially creating a decorator factory here, we are using the property of a call to be a callable,
we define the __call__ method here and when the class is called, that method will be invoked.

When we use the @DecoratorClass then an object is created with values of a and b passed to it, when we wrap a function
with that object then the function is passed as an input to the __call__ method of that class, the __call__ method takes
that function as an input and returns the closure function, having access to the attributes of the DecoratorClass.

"""

class DecoratorClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        print(f"Decorator class called with a={self.a}, b={self.b}")
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)

        return inner


@DecoratorClass(10, 20)
def add(a, b):
    return a+b


if __name__ == "__main__":
    print(add(2,5))
