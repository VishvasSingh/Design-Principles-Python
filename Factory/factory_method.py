"""
    Factory is a component responsible for wholesale creation of objects (not piecewise unlike Builders)

    ANY METHOD WHICH CREATES AN OBJECT IS CALLED FACTORY METHOD
"""

from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


