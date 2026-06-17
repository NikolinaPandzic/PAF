import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# podaci
kut = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40,
                45, 50, 55, 60, 65, 70, 75, 80, 85])

T_120 = np.array([
    0.8020, 0.8187, 0.8327, 0.8660, 0.8980,
    0.9153, 0.9293, 0.9653, 0.9747,
    1.0200, 1.0373, 1.1160, 1.1780,
    1.2733, 1.4180, 1.6373, 1.9100, 2.5460
])

T_240 = np.array([
    1.0140, 1.0320, 1.0433, 1.0673, 1.0840,
    1.1320, 1.1440, 1.1720, 1.1980,
    1.2293, 1.2813, 1.3573, 1.4200,
    1.5600, 1.7413, 1.9840, 2.4473,
    3.1573
])


g = 9.81

# stupnjevi -> radijani
kut_rad = np.radians(kut)


# teorijska funkcija
def period_njihala(kut, L):
    return 2*np.pi*np.sqrt(L/(g*np.cos(kut)))


# -------------------------
# curve_fit
# -------------------------

# traži duljinu L koja najbolje opisuje mjerenja

L120 = curve_fit(period_njihala, kut_rad, T_120)[0][0]

L240 = curve_fit(period_njihala, kut_rad, T_240)[0][0]


print("----- Njihalo 120 mm -----")
print("Dobivena duljina L =", L120, "m")

print()

print("----- Njihalo 240 mm -----")
print("Dobivena duljina L =", L240, "m")


# -------------------------
# relativna pogreška
# -------------------------

prava120 = 0.120
prava240 = 0.240

pogreska120 = abs(L120-prava120)/prava120*100
pogreska240 = abs(L240-prava240)/prava240*100


print()
print("Relativna pogreška 120 mm =", pogreska120, "%")
print("Relativna pogreška 240 mm =", pogreska240, "%")


# -------------------------
# graf
# -------------------------

kut_glatko = np.linspace(0, np.radians(85), 300)


plt.figure(figsize=(10,6))


# 120 mm
plt.scatter(kut, T_120, label="Mjerenja 120 mm")

plt.plot(np.degrees(kut_glatko),
         period_njihala(kut_glatko, L120),
         label="Fit 120 mm")


# 240 mm
plt.scatter(kut, T_240, label="Mjerenja 240 mm")

plt.plot(np.degrees(kut_glatko),
         period_njihala(kut_glatko, L240),
         label="Fit 240 mm")


plt.xlabel("Kut θ (°)")
plt.ylabel("Period T (s)")
plt.title("Ovisnost perioda njihala o kutu")
plt.grid()
plt.legend()

plt.show()