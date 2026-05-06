import numpy as np
import matplotlib.pyplot as plt

m = 9.11e-31

B = np.array([0, 0, 1])
E = np.array([0, 0, 0])

dt = 1e-13

def simulacija(q):

    v = np.array([1e5, 2e5, 3e5])
    r = np.array([0.0, 0.0, 0.0])

    x, y, z = [], [], []

    for i in range(4000):

        x.append(r[0])
        y.append(r[1])
        z.append(r[2])

        F = q * (E + np.cross(v, B))  #np.cross vektorski produkt
                                      #daje silu okomitu na brzinu
        a = F / m

        v = v + a * dt
        r = r + v * dt

    return x, y, z

# elektron i pozitron
x1, y1, z1 = simulacija(-1.6e-19)
x2, y2, z2 = simulacija( 1.6e-19)

# crtanje
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(x1, y1, z1, label="elektron")
ax.plot(x2, y2, z2, label="pozitron")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.legend() #razlikuje elektron i pozitron
plt.show()