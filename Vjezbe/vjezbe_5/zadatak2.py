
import numpy as np
import matplotlib.pyplot as plt
from calculus import pravokutna_aproksimacija, trapezna_metoda


def funkcija(x):
    return x**5 + 4*x + 1 


def analiticki_integral(a, b):
    F = lambda x: (1/6)*x**6 + 2*x**2 + x
    return F(b) - F(a)


a = 0
b = 5
br_koraka = [5, 10, 50, 100,150,200,300,500,1000,1500]

analiticko = analiticki_integral(a, b)
print('Analitička vrijednost integrala: ',analiticko)



rezultati_donja = []
rezultati_gornja = []
rezultati_trapezna = []

for n in br_koraka:
    donja, gornja = pravokutna_aproksimacija(funkcija, a, b, n)
    trapezna = trapezna_metoda(funkcija, a, b, n)
    rezultati_donja.append(donja)
    rezultati_gornja.append(gornja)
    rezultati_trapezna.append(trapezna)

plt.figure(figsize=(12, 8))
plt.plot(br_koraka, rezultati_donja, label='Pravokutna metoda (donja suma)', color='blue')
plt.plot(br_koraka, rezultati_gornja,  label='Pravokutna metoda (gornja suma)', color='orange')
plt.plot(br_koraka, rezultati_trapezna,label='Trapezna metoda', color='green')
plt.axhline(y=analiticko, color='red', linestyle='--', label='Analitička vrijednost')

plt.xlabel('Broj koraka')
plt.ylabel('Vrijednost integrala')
plt.title('Usporedba numeričke i analitičke integracije')
plt.legend()
plt.tight_layout()
plt.show()