
import matplotlib.pyplot as plt
from particle import Particle
import math
import numpy as np

v0 = 10
theta = 60
d_an = (v0**2 * math.sin(math.radians(2 * theta))) / 9.81


dt_vrijednosti= np.linspace(0.001, 0.1, 100)
Err= []


for dt in dt_vrijednosti:
    p = Particle(v0, theta)
    d_nu = p.range(dt)
    err = abs((d_nu - d_an) / d_an)
    Err.append(err)

plt.figure(figsize=(10,8))
plt.plot(dt_vrijednosti, Err)
plt.xlabel('∆t [s]')
plt.ylabel('Relativna pogreška')


plt.show()
