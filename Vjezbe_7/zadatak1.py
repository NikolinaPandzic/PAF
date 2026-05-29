import numpy as np

np.random.seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

def histogram(podaci, k):
    xmin = min(podaci)
    xmax = max(podaci)
    h = (xmax - xmin) / k
    
    rubovi = [xmin + i*h for i in range(k+1)]
    frekvencije = [0]*k

    for x in podaci:
        for i in range(k):
            if i < k-1:
                if rubovi[i] <= x < rubovi[i+1]:
                    frekvencije[i] += 1
                    break
            else:
                if rubovi[i] <= x <= rubovi[i+1]:
                   frekvencije[i] += 1

    for i in range(k):
        print(f"{i+1} [{rubovi[i]:.2f}, {rubovi[i+1]:.2f}) : {frekvencije[i]}")
    return rubovi, frekvencije, h

rubovi, frek, h = histogram(mase_ciste, 10)

import matplotlib.pyplot as plt

plt.bar(rubovi[:-1], frek, width=h, align='edge',edgecolor= 'black')
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram (ručno)")
plt.show()