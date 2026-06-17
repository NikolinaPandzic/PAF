import numpy as np

np.random.seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

def histogram(podaci, k):
    xmin = min(podaci) #najmanja masa u podacima
    xmax = max(podaci)
    h = (xmax - xmin) / k # sirina razreda
    
    rubovi = [] #prazna lista u koju se spremaju granice intervala
    for i in range(k+1):#Jer ako imam 10 intervala, treba mi 11 rubova
        rubovi.append(xmin + i*h)#min vrijednost+sirina razreda

    frekvencije = [] #koliko mjerenja pripada svakom razredu

    for i in range(k):#ovo prolazi kroz svaki interval
        broj = 0
        for x in podaci:#Ovo prolazi kroz svako pojedino mjerenje
            if i == k-1:
                if rubovi[i] <= x <= rubovi[i+1]: #jer zadnja najveća vrijednost nema gdje dalje otići
                    broj += 1
            else:
                if rubovi[i] <= x < rubovi[i+1]:
                    broj += 1

        frekvencije.append(broj)

    for i in range(k):
         print(i+1, rubovi[i], "-", rubovi[i+1], ":", frekvencije[i])
    return rubovi, frekvencije, h

rubovi, frekvencije, h = histogram(mase_ciste, 10)

import matplotlib.pyplot as plt

plt.bar( rubovi[:-1],frekvencije, width=h, align='edge',edgecolor= 'black')
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram (ručno)")
plt.show()