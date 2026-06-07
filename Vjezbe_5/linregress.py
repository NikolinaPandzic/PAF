import matplotlib.pyplot as plt
import math

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

n = len(M)

# izračun nagiba a (Dt)
suma_phi_m = 0
suma_phi2 = 0

for i in range(n):
    suma_phi_m += phi[i] * M[i]
    suma_phi2 += phi[i] ** 2

a = (suma_phi_m / n) / (suma_phi2 / n)

print("Dt =", a)

# pravac: y = a*x
x=phi
y_lin = []
for x in phi:
    y_lin.append(a * x)

y2_sr = sum(m**2 for m in M) / n
x2_sr = sum(p**2 for p in phi) / n

sigma_a = math.sqrt((1/n) * (y2_sr/x2_sr - a**2))

print('sigma:' , sigma_a)

plt.scatter(phi, M)       # točke
plt.plot(phi, y_lin)      # pravac

plt.xlabel("phi (rad)")
plt.ylabel("M (Nm)")
plt.title("Linearna regresija")

plt.show()