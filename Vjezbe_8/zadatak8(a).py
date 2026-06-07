import numpy as np
import matplotlib.pyplot as plt

h = np.array([0.14, 0.17, 0.19, 0.22, 0.25,
              0.28, 0.31, 0.34, 0.37, 0.40])

t = np.array([1.740, 1.793, 2.043, 2.190, 2.280,
              2.417, 2.540, 2.640, 2.670, 2.813])

x = np.log10(t)
y = np.log10(h)

n = len(x)

# formule 1 i 2
a = (n*np.sum(x*y)-np.sum(x)*np.sum(y)) / \
    (n*np.sum(x**2)-np.sum(x)**2)

b = (np.sum(y)-a*np.sum(x))/n


y_fit = a*x+b
s2 = np.sum((y-y_fit)**2)/(n-2)

sigma_a = np.sqrt(n*s2/(n*np.sum(x**2)-np.sum(x)**2))

sigma_b = np.sqrt(s2*np.sum(x**2)/(n*np.sum(x**2)-np.sum(x)**2))

print(f"a = {a:.4f} ± {sigma_a:.4f}")
print(f"b = {b:.4f} ± {sigma_b:.4f}")

# Graf
plt.scatter(x, y, label='Podaci')
plt.plot(x, y_fit, label='Linearni fit')
plt.xlabel('log(t)')
plt.ylabel('log(h)')
plt.legend()
plt.grid()
plt.show()