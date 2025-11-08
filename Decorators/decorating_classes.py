import datetime

"""
We can modify the behaviour of a class at runtime, we can add more attributes, methods and this process is called, 
Monkey patching, using a decorator we can monkeypatch classes and add properties and methods in them.
"""


def info(self):
    results = []
    results.append(f"time: {datetime.datetime.utcnow()}")
    results.append(f"Class: {self.__class__.__name__}")
    results.append(f"id: {hex(id(self))}")
    for k, v in vars(self).items():
        results.append(f"{k}:{v}")

    return results


def debug_info(cls):
    cls.debug_info = info
    return cls


@debug_info
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    p = Person('John', 25)
    print(p.debug_info())