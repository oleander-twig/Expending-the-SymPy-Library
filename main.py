import math
import sympy
import random
import decimal
import numpy as np
import matplotlib.pyplot as plt
from sympy import Rational
from sympy.geometry import Point
from sympy.core.symbol import _symbol


class Hyperbola:
    def __init__(self, hradious, vradious, angle=None):
        self.hradious = hradious
        self.vradious = vradious
        self.angle = angle

    @property
    def focus_distance(self):
        return (math.sqrt(self.hradious ** 2 + self.vradious ** 2))

    @property
    def foci(self):
        с = self.focus_distance
        return Point(с, 0), Point(-с, 0)

    @property
    def eccentricity(self):
        return (2 * self.focus_distance) / (2 * self.hradious)

    @property
    def equation(self, x='x', y='y'):
        x = _symbol(x, real=True)
        y = _symbol(y, real=True)
        t1 = (x / self.hradious) ** 2
        t2 = (y / self.vradious) ** 2
        return t1 - t2 - 1

    @property
    def asymptote(self, x='x'):
        x = _symbol(x, real=True)
        a1 = self.vradious / self.hradious * x
        a2 = - self.vradious / self.hradious * x
        return a1, a2

    def enclose_point(self, x1, y1):
        p = Point(x1, y1)
        if (x1 ** 2 / self.hradious - y1 ** 2 / self.vradious == 1):
            return True
        else:
            return False

    @property
    def random_point(self):
        y = random.uniform(- self.vradious, self.vradious)
        x = sqrt(self.hradious ** 2 * (y ** 2 + self.vradious ** 2) / self.vradious ** 2)
        return (x, y)

    def scale(self, x=1, y=1):
        if x:
            self.hradious = x * self.hradious
        if y:
            self.vradious = y * self.vradious
        return 0

    def draw(self, xmin, xmax):
        dx = 0.01
        xlist = np.around(np.arange(xmin, xmax, dx), decimals=4)
        y1list = np.sqrt((xlist ** 2 - self.hradious ** 2) * self.vradious ** 2 / self.hradious ** 2)
        y2list = - np.sqrt((xlist ** 2 - self.hradious ** 2) * self.vradious ** 2 / self.hradious ** 2)
        plt.plot(xlist, y1list)
        plt.plot(xlist, y2list)
        plt.title('Graph of the Hyperbola', fontsize=15)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.plot(xlist, y1list, color='blue')
        plt.plot(xlist, y2list, color='blue')
        plt.show()


hype = Hyperbola(1, 2)
hype.draw(-10, 10)