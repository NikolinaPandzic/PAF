import numpy as np
import matplotlib.pyplot as plt

# konstante
m = 9.11e-31
e = 1.602e-19

dt = 1e-13
N = 5000   #5000⋅10−13=5⋅10−10s

def simulacija(q, E, B):

    v = np.array([1e5, 2e5, 3e5], dtype=float)
    r = np.array([0.0, 0.0, 0.0]) #Početak koordinatnog sustava:r=(0,0,0)

    x, y, z = [], [], [] #spremanje trenutne pozicije

    for _ in range(N):

        x.append(r[0])
        y.append(r[1])
        z.append(r[2])

        F = q * (E + np.cross(v, B)) #Lorenzova sila
        a = F / m

        v = v + a * dt
        r = r + v * dt + 0.5 * a * dt**2

    return x, y, z


slucajevi = [
    ("E=(0,0,0)\nB=(0,0,1)",
     np.array([0, 0, 0]),
     np.array([0, 0, 1])),

    ("E=(1e5,0,0)\nB=(0,0,1)",
     np.array([1e5, 0, 0]),
     np.array([0, 0, 1])),

    ("E=(0,0,1e5)\nB=(0,0,1)",
     np.array([0, 0, 1e5]),
     np.array([0, 0, 1])),

    ("E=(0,0,0)\nB=(0,0,2)",
     np.array([0, 0, 0]),
     np.array([0, 0, 2]))
]

fig = plt.figure(figsize=(12, 10))

for i, (naslov, E, B) in enumerate(slucajevi, start=1):

    xe, ye, ze = simulacija(-e, E, B)
    xp, yp, zp = simulacija(+e, E, B)

    ax = fig.add_subplot(2, 2, i, projection='3d')

    ax.plot(xe, ye, ze, label='elektron')
    ax.plot(xp, yp, zp, label='pozitron')

    ax.set_title(naslov)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.legend(fontsize=8)

plt.tight_layout()
plt.show()