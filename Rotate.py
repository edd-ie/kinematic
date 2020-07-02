from sympy import symbols, cos, sin, pi, simplify, atan2, sqrt
from sympy.matrices import Matrix
import numpy as np

### Create symbols for joint variables which are commonly represented by "q"
### Joint variable "q" = "ϴ" or "d" [depending if the joint is revolute(ϴ) or prismatic(d)]
q1, q2, q3, q4 = symbols('q1:5') # can change symbols('q1:5') to symbols('x, y, z') remember slices do not include the end value 

# unrelated symbols can be defined like this:
A, R, O, C = symbols('A R O C')

# Conversion Factors
rtd = 180./np.pi # radians to degrees
dtr = np.pi/180. # degrees to radians

# Rotation matrices
R_x = Matrix([[1, 0, 0], [0, cos(q1), -sin(q1)], [0, sin(q1), cos(q1)]])
R_y = Matrix([[cos(q2), 0, sin(q2)], [0, 1, 0], [-sin(q2), 0, cos(q2)]])
R_z = Matrix([[cos(q3), -sin(q3), 0], [sin(q3), cos(q3), 0], [0, 0, 1]])

### A dictionary is passed to the symbolic expression and the evalf method evaluates it as a floating point
# The dictionary allows you to substitute multiples values simultaneously.
print("Rotation about the X-axis by 45-degrees")
print(R_x.evalf(subs={q1: 45*dtr})) # q1 is changed to 41
print("Rotation about the y-axis by 45-degrees")
print(R_y.evalf(subs={q2: 45*dtr})) # q1 is changed to 41
print("Rotation about the Z-axis by 30-degrees")
print(R_z.evalf(subs={q3: 30*dtr})) # q1 is changed to 41










