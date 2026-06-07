import numpy as np
import matplotlib.pyplot as plt

m = 0.5257      # kg
r = 4.025e-3    # m
g = 9.81        # m/s²

s = np.array([0.14, 0.17, 0.19, 0.22, 0.25,
              0.28, 0.31, 0.34, 0.37, 0.40])

t = np.array([1.740, 1.793, 2.043, 2.190, 2.280,
              2.417, 2.540, 2.640, 2.670, 2.813])

# ----- dio b -----

x = t**2
y = s

n = len(x)

a = (n*np.sum(x*y)-np.sum(x)*np.sum(y)) / \
    (n*np.sum(x**2)-np.sum(x)**2)

b = (np.sum(y)-a*np.sum(x))/n

print(f"a = {a:.6f}")
print(f"b = {b:.6f}")

# procjena pogreške nagiba
y_fit = a*x + b

s2 = np.sum((y - y_fit)**2)/(n - 2)

sigma_a = np.sqrt(
    n*s2/(n*np.sum(x**2)-np.sum(x)**2)
)

print(f"sigma_a = {sigma_a:.6f}")

# graf
plt.figure(figsize=(8,5))
plt.title('Ovisnost puta s o kvadratu vremena t²')
plt.scatter(x, y, label='Mjerenja')
plt.plot(x, y_fit, label='Linearni fit')
plt.xlabel(r'$t^2$ (s$^2$)')
plt.ylabel('s (m)')
plt.grid(True)
plt.legend()
plt.show()

# c

a_ef = 2*a
sigma_a_ef = 2*sigma_a

print(f"a_ef = {a_ef:.6f} ± {sigma_a_ef:.6f} m/s²")

I_z = (m*g*r**2)/a_ef - m*r**2

sigma_I_z = (m*g*r**2/a_ef**2) * sigma_a_ef

print(f"I_z = {I_z:.6e} kg·m²")
print(f"sigma_I_z = {sigma_I_z:.6e} kg·m²")