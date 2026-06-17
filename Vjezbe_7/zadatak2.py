import numpy as np

np.random.seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka
k=10
import matplotlib.pyplot as plt
plt.figure()
plt.hist(mase_ciste, k ,edgecolor= 'black')

mean = np.mean(mase_ciste)
median_np = np.median(mase_ciste)

plt.axvline(mean, linestyle='--', label='Sredina')
plt.axvline(median_np, linestyle='-', label='Medijan')

plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram (numpy)")
plt.legend()
plt.show()