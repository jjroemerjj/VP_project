# libraries to import
from scipy.optimize import fsolve
import math
import numpy as np


# ----------------------------------------------------------------
# Mechanism parameters - will be randomly changed each iteration
# ----------------------------------------------------------------

# bases coordinates
A = [0, 200]
B = [800, 0]

# arms length
AB = 400
BC = 800
CD = 800
BE = 400

# driving arm starting angle
fi = 45

# driving arm angular velocity
omega = 90

# ----------------------------------------------------------------
# equation formulation (this section has to be commented)
# ----------------------------------------------------------------

# general formula
# I1cos(fi1) + I2cos(fi2) + I3cos(fi3) + I4cos(fi4) + I5cos(fi5) = 0
# I1sin(fi1) + I2sin(fi2) + I3sin(fi3) + I4sin(fi4) + I5sin(fi5) = 0

# fi4 and fi5 are always fixed
# cos(fi4) = 0, cos(fi5) = 1, sin(fi4) = 0, cos(fi4) = 1

# general formula after simplification
# I1cos(fi1) + I2cos(fi2) + I3cos(fi3) + I5 = 0
# I1sin(fi1) + I2sin(fi2) + I3sin(fi3) + I4 = 0

# ----------------------------------------------------------------

# vector lengths calculation
I1 = AB
I2 = BC
I3 = CD
I4 = np.linalg.norm(B[0] - A[0])
I5 = np.linalg.norm(B[1] - A[1])

# I4, I5 vectors angle definition
fi4 = 180
fi5 = 90

# driving arm starting angle transformation to radians
fi1 = math.radians(fi)
fi4 = math.radians(fi4)
fi5 = math.radians(fi5)


# function defines system of equations
def f(p):
    fi2, fi3 = p
    e1 = I1*math.cos(fi1) + I2*math.cos(fi2) + I3*math.cos(fi3) + I4*math.cos(fi4) + I5*math.cos(fi5)
    e2 = I1*math.sin(fi1) + I2*math.sin(fi2) + I3*math.sin(fi3) + I4*math.sin(fi4) + I5*math.sin(fi5)
    return e1, e2


# solving system of equations
s = fsolve(f, np.array([0, 0]))

# convert to native python format (float)
s = getattr(s, "tolist", lambda: s)()

# converting angle from radians to degrees (s[0] = fi2, s[1] = fi3)
s[0] = math.degrees(s[0])
s[1] = math.degrees(s[1])

# Converting to positive-only angles
if s[0] < 0:
    s[0] = 360 - abs(s[0])

if s[1] < 0:
    s[1] = 360 - abs(s[1])

print(type(s))
print(s)


# ----------------------------------------------------------------
# Joint C position definition (vector)
# ----------------------------------------------------------------

# x-axis position
# Cx = AB*sin(fi1) + BC*sin(fi2)
# y-axis position
# Cy = AB*cos(fi1) + BC*cos(fi2)


# ----------------------------------------------------------------
# Input vector definition
# ----------------------------------------------------------------

