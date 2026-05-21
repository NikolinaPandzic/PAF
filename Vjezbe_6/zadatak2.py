import numpy as np
from zadatak1 import obradi_valjak
from zadatak1 import v1, v2, v3

def volumen_valjka(R, L): 
    return np.pi * R**2 * L

def sigma_volumena(R, sigma_R, L, sigma_L):
    return np.sqrt((2 * np.pi * R * L * sigma_R)**2 + (np.pi * R**2 * sigma_L)**2)

def u_cm(x_mm):
    return x_mm / 10

volumeni = [] 
sigme_V = []

for i, v in enumerate([v1, v2, v3], start=1):
    R_cm = u_cm(v[0]) 
    L_cm = u_cm(v[2]) 
    sigma_R_cm = u_cm(v[1]) 
    sigma_L_cm = u_cm(v[3])

    V = volumen_valjka(R_cm, L_cm) 
    sigma_V = sigma_volumena(R_cm, sigma_R_cm, L_cm, sigma_L_cm)

    volumeni.append(V) 
    sigme_V.append(sigma_V)

    print(f"Valjak {i}: V = {V:.3e} ± {sigma_V:.3e} cm^3")