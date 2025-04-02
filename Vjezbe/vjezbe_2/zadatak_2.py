import numpy as np
import matplotlib.pyplot as plt


v0 = int(input("Unesite iznos početne brzine: "))  
theta = int(input("Unesite kut otklona: ")) 

theta_rad = np.radians(theta)

g = 9.81

t_max = 10 
dt = 1 
t = np.arange(0, t_max+1, dt) 

v0x = v0 * np.cos(theta_rad)  
v0y = v0 * np.sin(theta_rad)

x = 0
y = 0
vx=v0x
vy=v0y

x_vrijednosti=[]
y_vrijednosti=[]
vx_vrijednosti=[]
vy_vrijednosti=[]

for i in t:
    x = v0x * i
    y = v0y * i - 0.5 * g * i**2
    vy=v0y-g*i
    x_vrijednosti.append(x)
    y_vrijednosti.append(y)
    vx_vrijednosti.append(v0x)
    vy_vrijednosti.append(vy)



plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x_vrijednosti, y_vrijednosti, label='x-y',color='purple')
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.title('Putanja čestice (x - y)')



plt.subplot(3, 1, 2)
plt.plot(t, x_vrijednosti, label='x-t', color='blue')
plt.xlabel('Vrijeme [s]')
plt.ylabel('X [m]')


plt.subplot(3, 1, 3)
plt.plot(t, y_vrijednosti, label='y-t', color='red')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Y [m]')


plt.tight_layout()
plt.show()





