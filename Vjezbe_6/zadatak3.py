import numpy as np
from zadatak1 import v1 ,v2 ,v3
from zadatak2 import volumeni , sigme_V

def gustoća(m, V): 
    return m / V

def sigma_gustoće(m, sigma_m, V, sigma_V): 
    return np.sqrt((sigma_m / V)**2 + (m * sigma_V / V**2)**2)

gustoce = [] 
sigme_rho = []
for i, v in enumerate([v1, v2, v3], start=1):
     m = v[4] 
     sigma_m = v[5] 
     
     V = volumeni[i-1] 
     sigma_V = sigme_V[i-1] 
     
     rho = gustoća(m, V) 
     sigma_rho = sigma_gustoće(m, sigma_m, V, sigma_V) 
     
     gustoce.append(rho) 
     sigme_rho.append(sigma_rho) 
     
     print(f"Valjak {i}: rho = {rho:.3f} ± {sigma_rho:.3f} g/cm^3")