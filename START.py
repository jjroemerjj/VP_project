# libraries to import
from sympy import *


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
omega = 20

# ----------------------------------------------------------------
# equation formulation
# ----------------------------------------------------------------

# general formula
# I1cos(fi1) + I2cos(fi2) + I3cos(fi3) + I4cos(fi4) + I5cos(fi5) = 0
# I1sin(fi1) + I2sin(fi2) + I3sin(fi3) + I4sin(fi4) + I5sin(fi5) = 0

# fi4 and fi5 are always fixed
# cos(fi4) = 0, cos(fi5) = 1, sin(fi4) = 0, cos(fi4) = 1

# general formula after simplification
# I1cos(fi1) + I2cos(fi2) + I3cos(fi3) + I5 = 0
# I1sin(fi1) + I2sin(fi2) + I3sin(fi3) + I4 = 0

# vector lengths calculation
I1 = AB
I2 = BC
I3 = CD
I4 = B[0] - A[0]
I5 = B[1] - A[1]

# driving arm starting angle calculation
fi1 = 45

fi2 = Symbol('fi2', real=True)
fi3 = Symbol('fi3', real=True)

e1 = Eq(I1*cos(fi1) + I2*cos(fi2) + I5)
p = solve([e1], fi2)

p = list(p[0])

print(type(p))
print(p)






#e1 = Eq(I1*cos(fi1) + I2*cos(fi2) + I3*cos(fi3) + I5)
#e2 = Eq(I1*sin(fi1) + I2*sin(fi2) + I3*sin(fi3) + I4)
#p = solve([e1, e2], fi2, fi3)


