import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Kutovi u stupnjevima
kut = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40,
                45, 50, 55, 60, 65, 70, 75, 80, 85])

# Periodi za l = 120 mm
period_120 = np.array([
    0.8020, 0.8187, 0.8327, 0.8660, 0.8980,
    0.9153, 0.9293, 0.9653, 0.9747,
    1.0200, 1.0373, 1.1160, 1.1780,
    1.2733, 1.4180, 1.6373, 1.9100, 2.5460
])

# Periodi za l = 240 mm
period_240 = np.array([
    1.0140, 1.0320, 1.0433, 1.0673, 1.0840,
    1.1320, 1.1440, 1.1720, 1.1980,
    1.2293, 1.2813, 1.3573, 1.4200,
    1.5600, 1.7413, 1.9840, 2.4473, 3.1573
])

kut_rad = np.radians(kut)

g = 9.81

# Teorijska funkcija
def period_njihala(kut_rad, duljina):
    return 2 * np.pi * np.sqrt(duljina / (g * np.cos(kut_rad)))

# Fit za l = 120 mm
parametri120, matrica_pogresaka120 = curve_fit(
    period_njihala,
    kut_rad,
    period_120
)

duljina120 = parametri120[0]
pogreska120 = np.sqrt(matrica_pogresaka120[0, 0])

# Fit za l = 240 mm
parametri240, matrica_pogresaka240 = curve_fit(
    period_njihala,
    kut_rad,
    period_240
)

duljina240 = parametri240[0]
pogreska240 = np.sqrt(matrica_pogresaka240[0, 0])

# Stvarne duljine
stvarna120 = 0.120
stvarna240 = 0.240

# Relativne pogreške
rel_pogreska120 = abs(duljina120 - stvarna120) / stvarna120 * 100
rel_pogreska240 = abs(duljina240 - stvarna240) / stvarna240 * 100

print("----- Njihalo 120 mm -----")
print(f"Duljina = {duljina120:.5f} ± {pogreska120:.5f} m")
print(f"Relativna pogreška = {rel_pogreska120:.2f} %")

print()

print("----- Njihalo 240 mm -----")
print(f"Duljina = {duljina240:.5f} ± {pogreska240:.5f} m")
print(f"Relativna pogreška = {rel_pogreska240:.2f} %")

kut_graf = np.linspace(0, np.radians(85), 500)

plt.figure(figsize=(10, 6))

plt.scatter(kut, period_120, label='Mjerenja (120 mm)')
plt.plot(
    np.degrees(kut_graf),
    period_njihala(kut_graf, duljina120),
    label=f'Fit 120 mm (l = {duljina120:.4f} m)'
)

plt.scatter(kut, period_240, label='Mjerenja (240 mm)')
plt.plot(
    np.degrees(kut_graf),
    period_njihala(kut_graf, duljina240),
    label=f'Fit 240 mm (l = {duljina240:.4f} m)'
)

plt.title('Ovisnost perioda njihala o kutu otklona')
plt.xlabel('Kut θ (°)')
plt.ylabel('Period T (s)')
plt.grid(True)
plt.legend()
plt.show()