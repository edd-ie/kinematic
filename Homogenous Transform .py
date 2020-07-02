from sympy import symbols, cos, sin, pi, simplify, atan2, sqrt
from sympy.matrices import Matrix
import numpy as np

"""Use of euler angles """

# Fixed Axis X-Y-Z Rotation Matrix
R_XYZ = Matrix([[0.353553390593274, -0.306186217847897, 0.883883476483184], 
               [0.353553390593274,  0.918558653543692, 0.176776695296637],
               [-0.866025403784439, 0.25, 0.433012701892219]])

######## TO DO ##########
# Calculate the Euler angles that produces a rotation equivalent to R (above)
r11 = R_XYZ[0,0]
r12 = R_XYZ[0,1]
r13 = R_XYZ[0,2]
r21 = R_XYZ[1,0]
r22 = R_XYZ[1,1]
r23 = R_XYZ[1,2]
r31 = R_XYZ[2,0]
r32 = R_XYZ[2,1]
r33 = R_XYZ[2,2]

# NOTE: Be sure your answer has units of DEGREES!
alpha = atan2(r21, r11)
beta  = atan2(-r31, sqrt((r11**2) + (r21**2)))
gamma = atan2(r32, r33)

print("Alpha =",alpha * rtd,"degrees or ", alpha, "radians")
print("BEta =",beta * rtd,"degrees or ", beta, "radians")
print("Gamma =",gamma * rtd,"degrees or ", gamma, "radians")




###############################################################
# Problem Statement:
  # Let P be a vector expressed in frame {B} with (x,y,z)
  # coordinates = (15.0, 0.0, 42.0)
  # Rotate P about the Y-axis by angle = 110 degrees. 
  # Then translate the vector 1 unit
  # in the X-axis and 30 units in the Z-axis. 
  # Print the new (x, y, z) coordinates of P after the transformation.  
###############################################################
#### Create symbols for joint variables
q1 = symbols('q1')

#### TO DO ####
# Replace P and T with appropriate expressions and calculate new coordinates of P in {A}. 
P = Matrix([15, 0, 4,1])     # P should be a 4x1 Matrix
T = Matrix([[cos(q1), 0, sin(q1), 1], [0, 1, 0, 0], [-sin(q1), 0, cos(q1), 30], [0, 0, 0, 1]])     # T Should be a 4x4 homogeneous Transform
P_new = simplify(T * P)
print("Homogeneous Transform about the X-axis by 110-degrees")
print(P_new.evalf(subs={q1: 110}))