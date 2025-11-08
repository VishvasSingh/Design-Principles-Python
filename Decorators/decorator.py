from functools import wraps


"""
@wraps(fn): Decorator to copy the function metadata to the function that is returned by the decorator, 

if we write a decorator without the @wraps decorator then debugging is difficult, if we were to call help() on the 
decorated function without the @wraps decorator then we get this:

-----------------------------------------------
Help on function inner in module __main__:

inner(*args, **kwargs)

-----------------------------------------------

But if we call it with the @wraps decorator then we get this output: 

-----------------------------------------------
Help on function add in module __main__:

add(a, b)
    Adds two numbers
    :param a: first number
    :param b: second number
    :return: sum of a and b

-----------------------------------------------

We can also use the inspect.signature(fn) on functions that were wrapped with decorators that used @wraps to copy  
function metadata

"""




def counter(fn):
    count = 0

    @wraps(fn)     # this decorator is used to copy the metadata of fn function to inner function, like name, docstring
                   # etc. this is quite useful while debugging, because when a decorator is used, it returns the
                   # modified function, so if we decorate fn function with counter decorator then all the information
                   # about fn function is going to be lost, because the decorator will essentially return the inner
                   # function, so using the wraps from functools module will help us solve that problem
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{fn.__name__} was called {count} times")
        return fn(*args, **kwargs)

    return inner


@counter
def add(a, b):
    """
    Adds two numbers
    :param a: first number
    :param b: second number
    :return: sum of a and b
    """
    return a + b

if __name__ == "__main__":
    res = add(1,2)
    print(help(add))