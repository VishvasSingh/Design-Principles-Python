class Logging:
    @staticmethod
    def log():
        return 'Logging'


class Serializable:
    def log(self):
        return 'Serializing ' + super().log()


class Displayable:
    def log(self):
        return 'Displaying ' + super().log()


class Widget(Displayable, Serializable, Logging):
    pass


if __name__ == '__main__':
    # Understanding why this outputs what it does is crucial
    print(Widget.mro())
    print(Widget().log())


"""

Above code is same as this ->

class Logging:
    @staticmethod
    def log():
        return 'Logging'


class Serializable(Logging):
    def log(self):
        return 'Serializing ' + super().log()


class Displayable(Serializable):
    def log(self):
        return 'Displaying ' + super().log()


class Widget(Displayable):
    pass


if __name__ == '__main__':
    # Understanding why this outputs what it does is crucial
    print(Widget.mro())
    print(Widget().log())

"""