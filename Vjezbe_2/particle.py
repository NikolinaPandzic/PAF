import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, kut, x0=0, y0=0):
        self.v0 = v0 
        self.kut = math.radians(kut)
        self.x0 = x0 
        self.y0 = y0 
        self.g = 9.81
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.kut)
        self.vy = self.v0 * math.sin(self.kut)

    def __move(self, dt):
        self.x += self.vx * dt         # x = x + vx*dt
        self.y += self.vy * dt         # y = y + vy*dt
        self.vy -= self.g * dt         # brzina pada zbog gravitacije

    def range(self, dt=0.01):
        self.reset()
        while self.y >= 0:             # dok je iznad tla
             self.__move(dt)
        return self.x
    
    def plot_trajectory(self, dt=0.01):
        self.reset()
        xs=[]
        ys=[]
        while self.y >= 0:
            xs.append(self.x)
            ys.append(self.y)
            self.__move(dt)

        plt.plot(xs,ys)
        plt.xlabel(f'x')
        plt.ylabel(f'y')
        plt.show()