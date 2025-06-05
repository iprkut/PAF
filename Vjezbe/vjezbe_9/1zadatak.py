
import numpy as np
import matplotlib.pyplot as plt


G = 6.67408e-11 
MS = 1.989e30  
MZ = 5.9742e24   


r_sunce = np.array([0.0, 0.0])
v_sunce = np.array([0.0, 0.0])
r_zemlja = np.array([1.486e11, 0.0])
v_zemlja = np.array([0.0, 29783.0])

dt = 60 * 60
koraci = int(365.242 * 24)

x_sunce = []
y_sunce = []
x_zemlja = []
y_zemlja = []

for i in range(koraci):
    r = r_zemlja - r_sunce
    udaljenost = (r[0]**2 + r[1]**2)**0.5  
    
    F = G * MS * MZ / udaljenost**2
    F_vektor = F * r / udaljenost
    
    a_sunce = F_vektor / MS
    v_sunce = v_sunce + a_sunce * dt
    r_sunce = r_sunce + v_sunce * dt
    a_zemlja = -F_vektor / MZ
    v_zemlja = v_zemlja + a_zemlja * dt
    r_zemlja = r_zemlja + v_zemlja* dt

    x_sunce.append(r_sunce[0])
    y_sunce.append(r_sunce[1])
    x_zemlja.append(r_zemlja[0])
    y_zemlja.append(r_zemlja[1])

plt.plot(x_sunce, y_sunce, label='Sunce')
plt.plot(x_zemlja, y_zemlja, label='Zemlja')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja Sunca i Zemlje')
plt.axis('equal')
plt.legend()
plt.show()