"""
    Factory is a component responsible for wholesale creation of objects (not piecewise unlike Builders)

    Factory method is an alternative to default initializers (__init__). It has advantages like:
        1. The code is more readable with meaningful function and argument names
        2. There is no complicated initialization logic in the init method
        3. We do not violate open closed principle in case we want to add more ways to initialize an object

    ANY METHOD WHICH CREATES AN OBJECT IS CALLED FACTORY METHOD
"""

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     """
    #         When the initialization is complex, we do not want to add conditions in init method and this would also
    #         break the open close principle in case we want to add more co-ordinate systems in future so to simply this
    #         it is better to use factories which help us with initialization of objects in different ways
    #     :param a: value of a
    #     :param b: value of b
    #     :param system: co-ordinate system
    #     """
    # if system == CoordinateSystem.CARTESIAN:
    #     self.x = a
    #     self.y = b
    #
    # elif system == CoordinateSystem.POLAR:
    #     self.x = a * sin(b)
    #     self.y = a * cos(b)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        # these kinds of methods are called factory methods, which help us initialize complete objects
        # here we created two factory methods, one for cartesian and one for polar point, we can hence
        # initialize the point in two different ways without complicating the init method of Point
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(2, 3)
    print(p, p2)
