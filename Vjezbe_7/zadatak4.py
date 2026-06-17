import numpy as np
import matplotlib.pyplot as plt

np.random.seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

from zadatak3 import medijan

srednja_ukupno = np.mean(mase)
medijan_ukupno = medijan(mase)

mu = np.mean(mase)
sigma = np.std(mase)

bez_outliera = [x for x in mase if abs(x - mu) <= 2*sigma]
srednja_bez = np.mean(bez_outliera)
medijan_bez = medijan(bez_outliera)

print("\n--- Rezultati ---")
print("Sredina (sve):", srednja_ukupno)
print("Medijan (sve):", medijan_ukupno)

print("Sredina (bez outliera):", srednja_bez)
print("Medijan (bez outliera):", medijan_bez)

print("\nPromjena sredine:", srednja_bez - srednja_ukupno)
print("Promjena medijana:", medijan_bez - medijan_ukupno)

# graf sve zajedno
plt.figure()
plt.hist(mase, bins=10, alpha=0.5,edgecolor= 'black')

plt.axvline(srednja_ukupno, linestyle='--',color='red', label='srednja (sve)')
plt.axvline(medijan_ukupno, linestyle='-',color='blue', label='medijan (sve)')
plt.axvline(srednja_bez, linestyle='--', color='orange', label='srednja (bez)')
plt.axvline(medijan_bez, linestyle='-',color='green', label='medijan (bez)')

plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.legend()
plt.show()