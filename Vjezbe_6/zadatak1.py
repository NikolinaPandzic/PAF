import numpy as np

#promjeri(mm)
valjak1_d = np.array([19.98, 20.18, 20.10, 20.08, 19.74]) 
valjak2_d = np.array([19.92, 19.82, 19.96, 19.98, 19.88]) 
valjak3_d = np.array([24.96, 24.98, 24.98, 24.92, 24.94])

# duljine (mm)
valjak1_L = np.array([49.80, 49.00, 50.48, 49.80, 49.96])
valjak2_L = np.array([52.56, 52.50, 52.62, 52.58, 52.54])
valjak3_L = np.array([55.34, 55.40, 55.30, 55.44, 55.48])

#mase(g)
valjak1_m = np.array([138.92, 138.98, 139.20, 138.90, 138.92])
valjak2_m = np.array([128.65, 128.60, 128.65, 128.35, 128.50])
valjak3_m = np.array([71.89, 71.90, 71.79, 71.85, 71.70])

def srednja(x): 
    return np.mean(x)

def sigma(x):
     n = len(x) 
     return np.sqrt(np.sum((x - srednja(x))**2) / (n * (n - 1)))

def obradi_valjak(d, L, m): 
    R = d / 2 
    
    R_mean = srednja(R) 
    R_sigma = sigma(R) 
    
    L_mean = srednja(L) 
    L_sigma = sigma(L) 
    
    m_mean = srednja(m) 
    m_sigma = sigma(m) 
    
    return R_mean, R_sigma, L_mean, L_sigma, m_mean, m_sigma

v1 = obradi_valjak(valjak1_d, valjak1_L, valjak1_m)
v2 = obradi_valjak(valjak2_d, valjak2_L, valjak2_m)
v3 = obradi_valjak(valjak3_d, valjak3_L, valjak3_m)

for i, v in enumerate([v1, v2, v3], start=1):
     print(f"\nValjak {i}:") 
     print(f"R = {v[0]:.4f} ± {v[1]:.4f} mm")
     print(f"L = {v[2]:.4f} ± {v[3]:.4f} mm") 
     print(f"m = {v[4]:.4f} ± {v[5]:.4f} g")