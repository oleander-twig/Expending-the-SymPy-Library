#!/usr/bin/env python
# coding: utf-8

# # Реализация класса Гипербола

# На официальном сайте SymPy.org можно запускать отдельные части кода, иллюстрирующие работу методов. Я поэксперементировала с .eccentricity и пришла к выводу, что это не является параметром класса. Это значение вычисляется. Поэтому в реализации класса Гипербола я тоже убрала этот параметр. 

# In[310]:


import sympy


class Hyperbola:
    def __init__(self, hradius, vradius, angle=None):
        if (angle != None):
            
        self.hradius = hradius
        self.vradius = vradius
        self.angle = angle
        
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    
hype = Hyperbola(4, 4, 0)
hype.eccentricity


# In[ ]:


Список фокусов гиперболы.


# In[375]:


import sympy
from sympy.geometry import Point


class Hyperbola:
    def __init__(self, hradius, vradius, angle=None):
        self.hradius = hradius
        self.vradius = vradius
        self.angle = angle
        
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
    
    @property
    def foci(self):
        return Point(self.focus_distance, 0), Point(- self.focus_distance, 0)
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    

hype = Hyperbola(2, 1, 0)
hype.foci


# На этом реализация атрибутов заканчивается. Переходим к методам. 
# Уравнение параболы в канонических координатах (=False) или более привычное уравнение глазу (=True).

# In[312]:


import sympy
from sympy.geometry import Point
from sympy import Symbol

class Hyperbola:
    def __init__(self, hradius, vradius, angle=None):
        self.hradius = hradius
        self.vradius = vradius
        self.angle = angle
        
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
    
    @property
    def foci(self):
        return Point(self.focus_distance, 0), Point(- self.focus_distance, 0)
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    
    def equation(self, x, y, evaluate=False):
        x = Symbol(x)
        y = Symbol(y)
        if (evaluate):
            t1 = (x * self.vradius) ** 2
            t2 = (y * self.hradius) ** 2
            return sympy.Eq(t2, t1 - 1 *(self.hradius * self.vradius) ** 2 )
        t1 = (x / self.hradius) ** 2
        t2 = (y / self.vradius) ** 2
        return sympy.Eq(t1 - t2, 1)
    

hype = Hyperbola(2, 7, 3)
eq = hype.equation('v', 't', True)
eq


# In[374]:


import sympy
from sympy.geometry import Point
from sympy import Symbol

class Hyperbola:
    def __init__(self, hradius, vradius, angle=None):
        self.hradius = hradius
        self.vradius = vradius
        self.angle = angle
        
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
    
    @property
    def foci(self):
        return Point(self.focus_distance, 0), Point(- self.focus_distance, 0)
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    
    def equation(self, x, y, evaluate=False):
        x = Symbol(x)
        y = Symbol(y)
        if (evaluate):
            t1 = (x * self.vradius) ** 2
            t2 = (y * self.hradius) ** 2
            return sympy.Eq(t2, t1 - 1 *(self.hradius * self.vradius) ** 2 )
        t1 = (x / self.hradius) ** 2
        t2 = (y / self.vradius) ** 2
        return sympy.Eq(t1 - t2, 1)
    
    def asymptote(self, x, y):
        x = Symbol(x)
        y = Symbol(y)
        a1 = self.vradius/self.hradius * x
        a2 = - self.vradius/self.hradius * x
        sympy.Eq(y, a1), sympy.Eq(y, a2)
        return sympy.Eq(y, a1), sympy.Eq(y, a2)
    
    

hype = Hyperbola(2, 1, 3)
eq1, eq2 = hype.asymptote('x', 'y')
eq2


# Проверка точки на принадлежность функции. 

# In[326]:


import sympy
from sympy.geometry import Point
from sympy import Symbol

class Hyperbola:
    def __init__(self, hradius, vradius, angle=None):
        self.hradius = hradius
        self.vradius = vradius
        self.angle = angle
        
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
    
    @property
    def foci(self):
        return Point(self.focus_distance, 0), Point(- self.focus_distance, 0)
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    
    def equation(self, x, y, evaluate=False):
        x = Symbol(x)
        y = Symbol(y)
        if (evaluate):
            t1 = (x * self.vradius) ** 2
            t2 = (y * self.hradius) ** 2
            return sympy.Eq(t2, t1 - 1 *(self.hradius * self.vradius) ** 2 )
        t1 = (x / self.hradius) ** 2
        t2 = (y / self.vradius) ** 2
        return sympy.Eq(t1 - t2, 1)
    
    def asymptote(self, x, y):
        x = Symbol(x)
        y = Symbol(y)
        a1 = self.vradius/self.hradius * x
        a2 = - self.vradius/self.hradius * x
        sympy.Eq(y, a1), sympy.Eq(y, a2)
        return sympy.Eq(y, a1), sympy.Eq(y, a2)
    
    def enclose_point(self, x1, y1):
        p = Point(x1, y1)
        if (x1 ** 2 / self.hradius - y1 ** 2 / self.vradius == 1):
            return True
        else:
            return False


hype = Hyperbola(2, 1, 3)
hype.enclose_point(0,0)


# Выбор рандомной точки, принадлежащей функции. 
# Координата y выбирается случайным образом из промежутка [-b;b]. Координата x вычисляется. 

# In[337]:


import sympy
import random
from sympy import Rational
from sympy.geometry import Point
from sympy import Symbol

class Hyperbola:
    def __init__(self, hradius, vradius, angle=None):
        self.hradius = hradius
        self.vradius = vradius
        self.angle = angle
        
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
    
    @property
    def foci(self):
        return Point(self.focus_distance, 0), Point(- self.focus_distance, 0)
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    
    def equation(self, x, y, evaluate=False):
        x = Symbol(x)
        y = Symbol(y)
        if (evaluate):
            t1 = (x * self.vradius) ** 2
            t2 = (y * self.hradius) ** 2
            return sympy.Eq(t2, t1 - 1 *(self.hradius * self.vradius) ** 2 )
        t1 = (x / self.hradius) ** 2
        t2 = (y / self.vradius) ** 2
        return sympy.Eq(t1 - t2, 1)
    
    def asymptote(self, x, y):
        x = Symbol(x)
        y = Symbol(y)
        a1 = self.vradius/self.hradius * x
        a2 = - self.vradius/self.hradius * x
        sympy.Eq(y, a1), sympy.Eq(y, a2)
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

    
hype = Hyperbola(3, 4, 3)
p = hype.random_point
p


# Масштабирование гиперболы. Метод scale будет принимать два не обязательных параметра (масштабирование x и масштабирование y)

# In[341]:


import sympy
import random
from sympy import Rational
from sympy.geometry import Point
from sympy import Symbol

class Hyperbola:
    def __init__(self, hradius, vradius, angle=None):
        self.hradius = hradius
        self.vradius = vradius
        self.angle = angle
        
    @property
    def focus_distance(self):
        return (sympy.sqrt(self.hradius ** 2 + self.vradius ** 2))
    
    @property
    def foci(self):
        return Point(self.focus_distance, 0), Point(- self.focus_distance, 0)
        
    @property
    def eccentricity(self):
        return self.focus_distance / self.hradius
    
    def equation(self, x, y, evaluate=False):
        x = Symbol(x)
        y = Symbol(y)
        if (evaluate):
            t1 = (x * self.vradius) ** 2
            t2 = (y * self.hradius) ** 2
            return sympy.Eq(t2, t1 - 1 *(self.hradius * self.vradius) ** 2 )
        t1 = (x / self.hradius) ** 2
        t2 = (y / self.vradius) ** 2
        return sympy.Eq(t1 - t2, 1)
    
    def asymptote(self, x, y):
        x = Symbol(x)
        y = Symbol(y)
        a1 = self.vradius/self.hradius * x
        a2 = - self.vradius/self.hradius * x
        sympy.Eq(y, a1), sympy.Eq(y, a2)
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
    

hype = Hyperbola(1, 2)
hype.scale(2, 3)
hype.equation('x', 'y', False)


# Построение графика функции. Метод Draw принимает два параметра:диапозон значений x, в пределах которых нужно построить функцию. (В перспективе есть идея сделать так же параметр, отвечающий за количество значений функции, своеобразная точность построения графика).
# Синтаксис обязывает задавать функцию y = ..., при выражения функции в таком виде появляется корень и получается, что y > 0, чтобы это поправить я сделала две функции: y = sqrt(); y = -sqrt(). 
# Также, модуль должен выводить сообщение об ошибке, если заданные значения икса не попали в ОДЗ. В данном случае, это промежутки (-inf; -a] && [a; inf). В дальнейшем это будет реализовано.

# In[379]:


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
        a1 = self.vradious/self.hradious * x
        a2 = - self.vradious/self.hradious * x
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
        
        
hype = Hyperbola(1,2)
hype.draw(-10, 10)


# 

# In[ ]:





# In[ ]:





# In[ ]:




