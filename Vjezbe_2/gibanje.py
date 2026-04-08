import particle
from particle import Particle
import math
p = Particle(10, 45)
num = p.range(0.001)

# analitička formula; R=(v0^2 * sin(2*theta))/g
R = (10**2 * math.sin(math.radians(90)))/9.81

print(f'Numericki:{num}')
print(f'Analiticki:{R}')
print(f'Greska:{abs(num-R)}')
p.plot_trajectory(0.001)