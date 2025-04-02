
#standardna devijacija-sirina oko srednje vrijednosti




import numpy as np
import math as m
import matplotlib.pyplot as plt

x=[12.5,3.2,58.475,4.5,2.3,0.1,67.9,0.8,43.70,10]

sum_x=0
for i in x:
    sum_x+=i


avg_x=sum_x/len(x)

sigma_x=0

for i in x:
    sigma_x+=((i-avg_x)**2)

sigma_x=m.sqrt(sigma_x/len(x))

plt.figure()
plt.plot(x,marker='o',markersize=5,c='black',label='Podaci')
plt.axhline(avg_x,c='red',label='avg_x')
plt.axhline(avg_x+sigma_x,c='red',label='sigma_x')
plt.axhline(avg_x-sigma_x,c='red')
plt.legend()


plt.show()