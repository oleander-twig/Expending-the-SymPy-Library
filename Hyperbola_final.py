#!/usr/bin/env python
# coding: utf-8

# In[264]:


import sympy
import random
import math
import decimal
import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol
from sympy import Rational
from sympy.geometry import Point
from sympy.core.symbol import _symbol


class Hyperbola:
    def __init__(self, hradius, vradius, angle=None, centre=None):
        self.hradius = hradius
        self.vradius = vradius
        self.angle = 0
        self.centre = Point(0,0)
        if angle:
            self.angle = angle
        if centre:
            self.centre = centre
    
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
    
    @property
    def foci(self):
        return Point(self.focus_distance, 0), Point(- self.focus_distance, 0)
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    
    def centre(self, x1, y1):
        self.centre = Point(x1, y1)
        return 0
    
    def equation(self, x, y, expression=False):
        x = Symbol(x)
        y = Symbol(y)
        x = x - self.centre[0]
        y = y - self.centre[1]
        x = x * sympy.cos(self.angle) + y * sympy.sin(self.angle)
        y = - x * sympy.sin(self.angle) + y * sympy.cos(self.angle)
        if not expression:
            t1 = (x * self.vradius) ** 2
            t2 = (y * self.hradius) ** 2
            return t2 - t1 - (self.hradius * self.vradius) ** 2 
        t1 = (x / self.hradius) ** 2
        t2 = (y / self.vradius) ** 2
        return sympy.Eq(t1 - t2, 1)
    
    def asymptote(self, x, y, expression=False):
        x = Symbol(x)
        y = Symbol(y)
        a1 = self.vradius/self.hradius * x
        a2 = - self.vradius/self.hradius * x
        if not expression:
            return y - a1, y - a2
        return sympy.Eq(y, a1), sympy.Eq(y, a2)
    
    def enclose_point(self, x1, y1):
        p = Point(x1, y1)
        if (x1 ** 2 / self.hradius - y1 ** 2 / self.vradius == 1):
            return True
        else:
            return False
    
    @property
    def random_point(self):
        y = random.uniform(- self.vradius, self.vradius)
        x = sympy.sqrt(self.hradius ** 2 * (y ** 2 + self.vradius ** 2) / self.vradius ** 2)
        return (x, y)
    
    def scale(self, x=1, y=1):
        if x:
            self.hradius = x * self.hradius
        if y:
            self.vradius = y * self.vradius
        return 0
    
    def draw(self, xmin, xmax):
        x = symbols('x')
        y = symbols('y')
        function = self.equation('x', 'y', False)
        as1, as2 = self.asymptote('x', 'y', False)
        p1 = plot_implicit(function, (x, xmin, xmax), title='Graph of the Hyperbola', line_color='blue', show=False)
        p2 = plot_implicit(as1, (x, xmin, xmax), line_color='crimson', show=False)
        p3 = plot_implicit(as2, (x, xmin, xmax), line_color='crimson', show=False)
        p1.append(p2[0])
        p1.append(p3[0])
        p1.show()
        
    def rotate(self, phi, measure=True):
        if not measure:
            phi = (phi * sympy.pi) / 180
        self.angle = phi
        return 0


# In[ ]:




