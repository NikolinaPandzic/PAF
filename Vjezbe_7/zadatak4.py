import numpy as np
import matplotlib.pyplot as plt

np.random.seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

from zadatak3 import medijan

mean_all = np.mean(mase)
median_all = medijan(mase)

# makni očite outliere
ciste = [x for x in mase if 1.8 < x < 2.3]

mean_clean = np.mean(ciste)
median_clean = medijan(ciste)

print("\n--- Rezultati ---")
print("Sredina (sve):", mean_all)
print("Medijan (sve):", median_all)

print("Sredina (bez outliera):", mean_clean)
print("Medijan (bez outliera):", median_clean)

print("\nPromjena sredine:", mean_clean - mean_all)
print("Promjena medijana:", median_clean - median_all)

# graf sve zajedno
plt.figure()
plt.hist(mase, bins=10, alpha=0.5,edgecolor= 'black')

plt.axvline(mean_all, linestyle='--', label='mean (sve)')
plt.axvline(median_all, linestyle='-', label='median (sve)')
plt.axvline(mean_clean, linestyle='--', label='mean (clean)')
plt.axvline(median_clean, linestyle='-', label='median (clean)')

plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Utjecaj outliera")
plt.legend()
plt.show()