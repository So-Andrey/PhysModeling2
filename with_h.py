import numpy as np
import math as mt
import matplotlib.pyplot as plt

Sx = 5 * pow(10, -2)
Sy = 0
Sz = mt.sqrt(1 - pow(Sx, 2))
S = np.array([Sx, Sy, Sz])
Hx = 0
Hy = 0
Hz = 100000
H = np.array([Hx, Hy, Hz])
h = 100000
m = 9.1093837 * pow(10,-31)
e = 1.602176634 * pow(10,-19)
a = 0.01
n = 1.25663706 * pow(10,-6)
y = e / m
w = 2 * y * n * Hz
dt = 5 * pow(10, -15)
t = 0
T = []
k = 0
l = 0
Sxarray = []

while (t <= 5e-9 and S[0]!= 0):
    H[2] = Hz - h * mt.sin(w * t)
    t += dt
    l = dt * (-y * n * np.cross(S, H) - a * y * n * np.cross(S,np.cross(S,H)))
    S += l
    S /= np.linalg.norm(S)
    k += 1
    if (k == 999):
        T.append(t)
        Sxarray.append(S[0])
        k = 0

plt.figure()
plt.plot(T, Sxarray)
plt.xlabel(r't, c')
plt.ylabel(r'Sx, м')
plt.grid(True)
plt.show()