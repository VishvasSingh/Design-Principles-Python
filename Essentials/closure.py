"""
What Is a Closure?
A closure in Python is a nested function that retains access to variables from its enclosing (outer) function's scope,
even after the outer function has finished executing. Closures allow inner functions to "remember" and use variables
from their surrounding environment, creating functions with extended scopes that preserve state information


How Closures Are Created
A closure is formed when three conditions are met:

A function is defined inside another function (nested function)
The inner function references variables from the outer function
The outer function returns the inner function


Key Benefits

Closures provide several advantages:
Data encapsulation: They help avoid using global variables and provide data hiding
State retention: They preserve state information between consecutive function calls
Decorator implementation: They are fundamental to creating Python decorators

"""

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{fn.__name__} was called {count} times")
        return fn(*args, **kwargs)

    return inner


def add (a, b):
    return a+b

if __name__ == "__main__":
    add_wrapper = counter(add)
    add_wrapper(1,2)
    add_wrapper(4,5)