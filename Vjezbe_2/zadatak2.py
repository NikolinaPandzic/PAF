import particle
from particle import Particle
import math
import matplotlib.pyplot as plt

v0=10
kut=60
g=9.81
R = (v0**2 * math.sin(math.radians(2*kut)))/g
dt_vrijednost=[]
greske=[]
dt=0.001
while dt <= 0.1:
    p = Particle(v0, kut)
    num = p.range(dt)
    greska = (abs(R-num)/R)
    dt_vrijednost.append(dt)
    greske.append(greska)
    dt += 0.0005 #gusce

plt.plot(dt_vrijednost, greske)
plt.xlabel(f'dt')
plt.ylabel(f'Relativna pogreska')
plt.title(f'Ovisnost pogreske o dt')
plt.grid()
plt.show()