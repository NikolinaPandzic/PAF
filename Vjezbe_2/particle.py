import math
import matplotlib.pyplot as plt

class Particle:

    def __init__(self, v0, kut, x0=0, y0=0):
        # spremanje početnih vrijednosti
        self.v0_init = v0
        self.kut_init = kut
        self.x0_init = x0
        self.y0_init = y0
        self.reset()

    def reset(self):
        # vraća česticu na početno stanje
        self.v0 = self.v0_init
        self.kut = math.radians(self.kut_init)

        self.x = self.x0_init
        self.y = self.y0_init

        self.vx = self.v0 * math.cos(self.kut)
        self.vy = self.v0 * math.sin(self.kut)

        self.g = 9.81

    def __move(self, dt):
        # pomak čestice za mali vremenski korak dt
        self.x += self.vx * dt
        self.y += self.vy * dt - 0.5 * self.g * dt**2
        self.vy -= self.g * dt

    def range(self, dt):
        # numerički računa domet
        self.reset()

        while self.y >= 0:
            self.__move(dt)

        return self.x

    def plot_trajectory(self, dt):
        # crta putanju projektila
        self.reset()

        x_lista = []
        y_lista = []

        while self.y >= 0:
            x_lista.append(self.x)
            y_lista.append(self.y)
            self.__move(dt)

        plt.plot(x_lista, y_lista)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("Putanja projektila")
        plt.grid(True)
        plt.show()