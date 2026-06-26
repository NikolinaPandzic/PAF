import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
G = 6.67430e-11
AU = 1.496e11
dt = 86400

class Planet:
    def __init__(self, ime, masa, x, y, vx, vy):
        self.ime = ime
        self.masa = masa
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0

        self.putanja = [[x,y]]

class Universe:
    def __init__(self):
        self.planeti = []

    def dodaj_planet(self, planet):
        self.planeti.append(planet)

    def evolucija(self):

        for p in self.planeti:

            ax = 0
            ay = 0

            for drugi in self.planeti:

                if p != drugi:
                    #smjer prema drugom planetu
                    dx = drugi.x - p.x
                    dy = drugi.y - p.y
                    r = np.sqrt(dx**2 + dy**2)

                    ax += G * drugi.masa * dx / r**3
                    ay += G * drugi.masa * dy / r**3

            p.vx += ax * dt
            p.vy += ay * dt

            p.x += p.vx * dt
            p.y += p.vy * dt

            p.putanja.append([p.x, p.y])

# planeti
sunce = Planet("Sunce", 1.989e30, 0, 0, 0, 0)

merkur = Planet("Merkur", 3.285e23,
                0.387*AU, 0, 0, 47870)

venera = Planet("Venera", 4.867e24,
                0.723*AU, 0, 0, 35020)

zemlja = Planet("Zemlja", 5.972e24,
                AU, 0, 0, 29780)

mars = Planet("Mars", 6.39e23,
              1.524*AU, 0, 0, 24070)


svemir = Universe()

for p in [sunce, merkur, venera, zemlja, mars]:
    svemir.dodaj_planet(p)

# 5 godina
for i in range(365*5):
    svemir.evolucija()

plt.figure(figsize=(7,7))

for p in svemir.planeti:

    put = np.array(p.putanja)

    plt.plot(
        put[:,0]/AU,
        put[:,1]/AU,
        label=p.ime
    )
    plt.scatter(
    put[-1,0]/AU,
    put[-1,1]/AU
)
plt.axis("equal")
plt.grid()
plt.legend()
plt.xlabel("x [AU]")
plt.ylabel("y [AU]")
plt.title("Putanje planeta nakon 5 godina")

plt.show()

fig, ax = plt.subplots(figsize=(7,7))

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect("equal")

ax.grid()

tocke = []
tragovi = []
for p in svemir.planeti:

    trag, = ax.plot([],[])
    toc, = ax.plot([],[],"o",label=p.ime)

    tragovi.append(trag)
    tocke.append(toc)

ax.legend()
def animacija(i):

    for j,p in enumerate(svemir.planeti):

        put = np.array(p.putanja[:i+1])


        tragovi[j].set_data(
            put[:,0]/AU,
            put[:,1]/AU
        )

        tocke[j].set_data(
            [put[-1,0]/AU],
            [put[-1,1]/AU]
        )
    return tragovi + tocke

ani = FuncAnimation(
    fig,
    animacija,
    frames=365*5,
    interval=20,
    blit=True
)
plt.show()