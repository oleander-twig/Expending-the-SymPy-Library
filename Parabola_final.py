#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sympy
import random
from sympy import symbols
from sympy import Symbol
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


class Parabola:
    def __init__(self, focus, direct, par, angle=None):
        self.focus = focus
        self.direct = direct
        self.par = par
    
    @property
    def eccentricity(self):
        return 1
    
    def equation(self, x, y, expression=False):
        x = Symbol(x)
        y = Symbol(y)
        t1 = 2 * self.par * x
        t2 = y ** 2
        if not expression:
            return t2 - t1
        return sympy.Eq(t2, t1)
    
    def scale(self, p):
        self.par = p * self.par
        return 0
    
    @property
    def random_point(self):
        x = random.uniform(0, 100)
        y = sympy.sqrt(2 * self.par * x)
        return (x, y)
    
    @property
    def draw(self):
        x = symbols('x')
        y = symbols('y')
        function = self.equation('x', 'y', False)
        p1 = plot_implicit(function, title='Graph of the Parabola', line_color='blue')


# In[ ]:




