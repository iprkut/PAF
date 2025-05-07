import numpy as np
import matplotlib.pyplot as plt
import calculus as cals


def kubna(x):
    return x**3


def sinus(x):
    return np.sin(x)



x_kubna, derivacije_kubne = cals.derivacija_u_rasponu(kubna, -2, 2)

x_sinus,derivacije_sinusa = cals.derivacija_u_rasponu(sinus, 0, 2 * np.pi)

    
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_kubna, derivacije_kubne, label="Numerička derivacija")
plt.title("Derivacija kubne funkcije")
plt.legend()



plt.subplot(1, 2, 2)
plt.plot(x_sinus,derivacije_sinusa, label="Numerička derivacija")
plt.title("Derivacija sinus funkcije")
plt.legend()

plt.tight_layout()
plt.show()
