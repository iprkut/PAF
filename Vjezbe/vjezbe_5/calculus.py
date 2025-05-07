
import numpy as np

#derivacija

def derivacija_u_tocki(funkcija, x, korak=0.01):
        return (funkcija(x + korak) - funkcija(x)) / korak
    

def derivacija_u_rasponu(funkcija, donja_granica, gornja_granica, korak=0.01):
    x_vrijednosti =np.linspace(donja_granica,gornja_granica,1000)
    derivacije = []
    for x in x_vrijednosti:
        derivacije.append(derivacija_u_tocki(funkcija, x, korak))
    return x_vrijednosti, derivacije
    je


#Integriranje

def pravokutna_aproksimacija(funkcija, a, b, n):
    dx = (b - a) / n
    donja_suma = 0
    gornja_suma = 0
    for i in range(n):
        x_donji = a + i * dx
        x_gornji = a + (i + 1) * dx
        donja_suma += funkcija(x_donji)
        gornja_suma += funkcija(x_gornji)
    donji_integral = donja_suma * dx
    gornji_integral = gornja_suma * dx
    return donji_integral, gornji_integral

def trapezna_metoda(funkcija, a, b, n):
    dx = (b - a) / n
    suma = 0.5 * (funkcija(a) + funkcija(b))
    for i in range(1, n):
        x = a + i * dx
        suma += funkcija(x)
    return suma * dx