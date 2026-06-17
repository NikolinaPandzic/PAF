import numpy as np
from zadatak1 import obradi_valjak
from zadatak3 import gustoce
#sa interneta uzete gustoće elemenata
rho_tablica = {
    "bakar": 8.96,
    "željezo": 7.87,
    "aluminij": 2.70
}

for i in range(3):
    rho = gustoce[i] #uzima gustocu iz liste
#Usporedila sam izmjerenu gustoću s literaturnim vrijednostima i odabrala materijal čija je gustoća najbliža eksperimentalnoj.
    materijal = min(rho_tablica, key=lambda x: abs(rho - rho_tablica[x]))
    #Lambda funkcija koja ovdje računa koliko je gustoća pojedinog materijala udaljena od izmjerene gustoće
    rho_lit = rho_tablica[materijal]

    delta = abs(rho - rho_lit) / rho_lit * 100

    print(f"Valjak {i+1}:")
    print(f"  materijal: {materijal}")
    print(f"  relativna pogreška = {delta:.2f} %")