


from particle import Particle
import math


v0 = 10
theta = 60 

#analitički domet(preko formule)
d_an= (v0**2 * math.sin(math.radians(2 * theta))) / 9.81


p = Particle(v0, theta)

#numerički domet
d_nu = p.range()  

print()
print('Analitički domet: ',d_an)
print('Numerički domet:  ',d_nu)
print('Odstupanje: ',abs((d_nu-d_an)/d_an)*100)


p.plot_trajectory()
