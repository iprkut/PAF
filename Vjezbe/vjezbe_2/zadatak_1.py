import numpy as np
import matplotlib.pyplot as plt

F = int(input("Unesite iznos sile: "))  
m = int(input("Unesite masu čestice: ")) 

t_max = 10 
dt = 1
t = np.arange(0, t_max+1, dt) 

x0 = 0 
v0 = 0  
a = F / m 

brzine=[]
pomaci=[]
akceleracija=[]


x = x0
v = v0
for i in range(len(t)):
    if i == 0:
        brzine.append(v0)
        pomaci.append(x0)
        akceleracija.append(a)
    else:
        v = v + a * dt  
        x = x + v * dt + 0.5 * a * dt**2  
        brzine.append(v)
        pomaci.append(x)
        akceleracija.append(a)



plt.figure(figsize=(12, 8))


plt.subplot(3, 1, 1)
plt.plot(t, pomaci, label='Položaj (x)', color='blue')
plt.xlabel('Vrijeme (t) [s]')
plt.ylabel('Položaj (x) [m]')


plt.subplot(3, 1, 2)
plt.plot(t, brzine, label='Brzina (v)', color='red')
plt.xlabel('Vrijeme (t) [s]')
plt.ylabel('Brzina (v) [m/s]')

plt.subplot(3, 1, 3)
plt.plot(t, akceleracija, label='Akceleracija (a)', color='green')
plt.xlabel('Vrijeme (t) [s]')
plt.ylabel('Akceleracija (a) [m/s^2]')


plt.tight_layout()
plt.show()
