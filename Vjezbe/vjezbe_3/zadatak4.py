
import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336]) 
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]) 


sum_x2 = np.sum(phi**2)
sum_xy = np.sum(phi * M)
sum_y2 = np.sum(M**2)
n = len(M)

a = sum_xy / sum_x2 
sigma_a = np.sqrt((1/n) * (sum_y2 / sum_x2 - a**2)) 

plt.plot(phi, a * phi, color='blue')
plt.xlabel('Kut φ (rad)')
plt.ylabel('Moment M (Nm)')
plt.show()


