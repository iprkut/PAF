

import matplotlib.pyplot as plt
import math

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #Nm 
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #rad 
n = len(phi)


sum_x2 = sum(x**2 for x in phi)
sum_xy = sum(x*y for x, y in zip(phi, M))
sum_y2 = sum(y**2 for y in M)


a = sum_xy / sum_x2

sigma_a = math.sqrt((1/n) * ((sum_y2 / sum_x2) - a**2))


print(a,sigma_a)

M_fit = [a * x for x in phi]

plt.plot(phi, M, 'o')
plt.plot(phi, M_fit, '-')
plt.xlabel('Kut φ (rad)')
plt.ylabel('Moment M (Nm)')


plt.show()