 
import matplotlib.pyplot as plt
import numpy as np
def jednadzba_pravca(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    return k,l

def graf():
    x1 = int(input('Upiši vrijednost x1: '))
    y1 = int(input('Upiši vrijednost y1: '))
    x2 = int(input('Upiši vrijednost x2: '))
    y2 = int(input('Upiši vrijednost y2: '))
    jednadzba_pravca(x1,y1,x2,y2)
    k,l = jednadzba_pravca(x1,y1,x2,y2)
    x_vrijednosti = [x1 - 1, x2 + 1] 
    y_vrijednosti = [k* x + l for x in x_vrijednosti]
    x_range=np.linspace(min(x_vrijednosti)-1,max(x_vrijednosti)+1)
    y_range=k*x_range + l
    plt.plot(x_range,y_range)
    plt.scatter([x1,x2],[y1,y2],color='red')

    
    odabir = input("Želite li spremiti graf kao PDF? (da/ne): ").strip().lower()
    if odabir == 'da':
        ime_datoteke = input("Unesite ime datoteke (s nastavkom .pdf): ")
        plt.savefig(ime_datoteke) 
        print(f'Graf je spremljen')
    else:
        plt.show()


graf()
