from sympy import symbols, cos, sin, pi, simplify, atan2, sqrt
from sympy.matrices import Matrix
import numpy as np


### Create symbols for joint variables
# The numbers 1 to 4 correspond to each rotation in the order specified to you.
q1, q2, q3, q4 = symbols('q1:5')

### Define functions for Rotation Matrices about x, y, and z given specific angle.
def rot_x(q):
    R_x = Matrix([[ 1,              0,        0],
                  [ 0,         cos(q),  -sin(q)],
                  [ 0,         sin(q),  cos(q)]])
    
    return R_x
    
def rot_y(q):              
    R_y = Matrix([[ cos(q),        0,  sin(q)],
                  [      0,        1,       0],
                  [-sin(q),        0, cos(q)]])
    
    return R_y

def rot_z(q):    
    R_z = Matrix([[ cos(q),  -sin(q),       0],
                  [ sin(q),   cos(q),       0],
                  [      0,        0,       1]])
    
    return R_z
              


### Define rotations between frames
# Initial Rotation Matrix for Frame A
Ra = Matrix([[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]])


# Rotations performed on individual Frames for A->B->E
Rb_a = rot_y(q1)  # Rotate A 90 degrees on y-axis
Re_b = rot_x(q2)  # Rotate B 90 degrees on x-axis

# Rotations performed on individual Frames for A->C->D->E
Rc_a = Ra  # No rotaion, thus RA stays sames
Rd_c = rot_x(q3)  # Rotate C 90 degrees on x-axis
Re_d = rot_z(q4)  # Rotate D 90 degrees on z-axis

### Define Translations between frames.

tb_a = Matrix([ [-2],  [2], [4]])  # 3x1 matrix for traslating A-B
te_b = Matrix([  [0],  [2], [0]])  # 3x1 matrix for traslating B-E
tc_a = Matrix([  [4],  [4], [0]])  # 3x1 matrix for traslating A-C
td_c = Matrix([ [-3],  [3], [2]])  # 3x1 matrix for traslating C-D
te_d = Matrix([ [-3],  [2], [3]])  # 3x1 matrix for traslating D-E

### Define homogenous transformation matrices
#  .row_join() -- Adds a row to a matrix
#  .col_join() -- Adds a column to a matrix

Ta = Ra.row_join(Matrix([[0], [0], [0]]))
Ta = Ta.col_join(Matrix([[0, 0, 0, 1]])) 

Tb_a = Rb_a.row_join(tb_a)
Tb_a = Tb_a.col_join(Matrix([[0, 0, 0, 1]]))

Te_b = Re_b.row_join(te_b)
Te_b = Te_b.col_join(Matrix([[0, 0, 0, 1]]))

Tc_a = Rc_a.row_join(tc_a)
Tc_a = Tc_a.col_join(Matrix([[0, 0, 0, 1]]))

Td_c = Rd_c.row_join(td_c)
Td_c = Td_c.col_join(Matrix([[0, 0, 0, 1]]))

Te_d = Re_d.row_join(te_d)
Te_d = Te_d.col_join(Matrix([[0, 0, 0, 1]]))               

### Composition of Transformations
Te_a_1 = simplify(Ta * Tb_a * Te_b)

Te_a_2 = simplify(Ta * Tc_a * Td_c * Te_d)

### Calculate orientation and position for E
E_1 = Te_a_1.evalf(subs={q1: -pi/2, q2: pi/2}, chop = True)

E_2 = Te_a_2.evalf(subs={q3: pi/2, q4: pi/2}, chop = True)

print("Transformation Matrix for A->B->E:")
print(E_1)

print("Transformation Matrix for A->C->D->E:")
print(E_2)


if E_1 == E_2:
  print("True")
# elif E_1 > E_2:
#   Eq = E_1 - E_2
#   print("E_1 is larger by: ", Eq)
# elif E_2 > E_1:
#   Eq = E_2 - E_1
#   print("E_2 is larger by: ", Eq)
else:
  print("false")