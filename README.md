# Expending the SymPy Library
SymPy is a Python library for symbolic mathematics. 
This project aims to expend the liabrary functionality by implementing Parabola and Hyperbola classes. The project is written entirely in Python.

## Hyperbola Features
``` 
class Hyperbola (hradius=None, vradius=None, centre=None, angle=None, 
                eccentricity=None, foci=None, focus_distance=None)
```
 
### Parameters:
- **Eccentricity**: number, Optional 
- **Foci**: List, Optional 
- **Focus_distance**: number, Optional
- **Hradious**: number or SymPy expression
- **Vradious**: number or SymPy expression
- **Angle**: number 
    Rotates a function. Default value is 0 rad.
- **Centre**: Point, optional 
         Default value is Point(0, 0).

### Methods
``` equation(x=None, y=None, expression=False): ```
Returns the equation of hyperbola using given symbols. If expression is true the equation has regular type, otherwise it is canonical. 

``` asymptote(x=None, y=None): ```
Returns a set of hyperbola asymptotes using given symbols.

```order_point(x1=1, y1=1): ```
Return True if the point belongs to Hyperbola, else - return False. 

```random_point(): ```
Returns a random point, which belongs to Hyperbola.

```scale(x1=1, y1=1): ```
Scales hyperbola within geven parameters. 

```draw(xmin=1, xmax=2, ymin=1, ymax=2): ```
Draws function with asymptotes in the given range. 

```rotate(a=0): ```
Changes the parameter `angle`. 

```move(x1=0, y1=0): ```
Changes the parameter `centre`. 

_**All methods will be automatically recalculated if the angle or centre were changed.**_  

## Parabola Features
``` 
class Parabola (focus=None, direct=None, semilatus=None, 
                angle=None, eccentricity=None)
```

### Parameters:
- **Direct** : SymPy expression
- **Focus**: number
- **Semilatus**: number
- **Eccentricity**: number, Optional 
- **Angle**: number, Optional
    Rotates a function. Default value is 0 rad.

### Methods
``` equation(x=None, y=None, expression=False): ```
Returns the equation of hyperbola using given symbols. If expression is true the equation has regular type, otherwise it is canonical. 

```scale(x1=1): ```
Scales hyperbola within a geven parameter. 

```random_point(): ```
Returns a random point, which belongs to Parabola.

```draw(): ```
Draws a function.

```rotate(a=0): ```
Changes the parameter `angle`. 

_**All methods will be automatically recalculated if the angle or centre were changed.**_

