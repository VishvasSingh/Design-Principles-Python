from functools import wraps
from time import perf_counter

"""
If we want to create decorators that take in input parameters then we need to use decorator factories,
decorator factories return a decorator when they are called, they are not themselves a decorator, they create the
decorator with the passed in parameters when they are called. 

if we try to create a decorator in the below way:

def timed(fn, reps):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter()-start)
        avg_elapsed = total_elapsed/reps
        print(f'avg time -> {avg_elapsed}')
        return result
        
    return inner
    
then calling a decorator in this way would work:
my_func = timed(my_func, 10)

but calling a decorator in this way would not work:

@timed(10)
def my_func():


that's why we need a decorator factory, essentially what we are trying to achieve is that we need a decorator with the 
passed in parameters dynamically 
"""


def decorator_factory(reps):

    def decorator(fn):

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            result = None
            for i in range(reps):
                print(f"run no {i}")
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(f'avg time -> {avg_elapsed}')
            return result

        return inner

    return decorator


@decorator_factory(5)
def add(a, b):
    return a+b


if __name__ == "__main__":
    add(2,3)




