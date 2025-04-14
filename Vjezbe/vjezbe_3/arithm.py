
import math
import numpy as np

def aritmeticka_sredina(podaci):
    return sum(podaci) / len(podaci)

def standardna_devijacija(podaci):
    n = len(podaci)
    a_s= aritmeticka_sredina(podaci)
    suma_kvadrata = sum((x - a_s) ** 2 for x in podaci)
    return math.sqrt(suma_kvadrata / (n * (n - 1)))


podaci = [12, 15, 14, 10, 8, 17, 19, 21, 11, 16]
print( aritmeticka_sredina(podaci))
print(standardna_devijacija(podaci))


print(np.mean(podaci))
print(np.std(podaci, ddof=1) / math.sqrt(len(podaci)))