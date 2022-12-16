from math import sin, cos
from enum import Enum


class CoordinateSystem(Enum):
    cartesian = 1
    polar = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


p = Point(1, 2)
p2 = Point.new_polar_point(3, 4)
print(p, p2)
