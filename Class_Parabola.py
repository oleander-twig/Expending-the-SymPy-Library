#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sympy
import random
from sympy import symbols
from sympy import Symbol
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


class Parabola:
    def __init__(self, focus, direct, semilatus, angle=None):
        self.focus = focus
        self.direct = direct
        self.semilatus = semilatus
        self.angle = 0
        if angle:
            self.angle = angle
    
    @property
    def eccentricity(self):
        return 1
    
    def equation(self, x=None, y=None, expression=False):
        if x:
            x = Symbol(x)
        else:
            x = symbols('x')
        if y:
            y = Symbol(y)
        else:
            y = symbols('y')
        x = x * sympy.cos(self.angle) + y * sympy.sin(self.angle)
        y = - x * sympy.sin(self.angle) + y * sympy.cos(self.angle)
        t1 = 2 * self.semilatus * x
        t2 = y ** 2
        if not expression:
            return t2 - t1
        return sympy.Eq(t2, t1)
    
    def scale(self, p):
        self.semilatus = p * self.semilatus
        return 0
    
    @property
    def random_point(self):
        x = random.uniform(0, 100)
        y = sympy.sqrt(2 * self.semilatus * x)
        return (x, y)
    
    @property
    def draw(self):
        x = symbols('x')
        y = symbols('y')
        function = self.equation('x', 'y', False)
        p1 = plot_implicit(function, title='Graph of the Parabola', line_color='blue')
        
    def rotate(self, phi):
        self.angle = phi

