import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, angle, Cd=0.47, rho=1.225, A=0.01, m=1.0, g=9.81):
        self.v0 = v0
        self.angle = np.radians(angle) #pretvara stupnjeve u radijane
        self.Cd = Cd  #koeficijent otpora zraka
        self.rho = rho #gustoća zraka(kg/m^3)
        self.A = A #površina presjeka
        self.m = m
        self.g = g
        #Spremamo sve fizičke parametre u objekt, da ih možemo koristiti u simulaciji
        #formula za otpor zraka
        self.otpor = 0.5 * Cd * rho * A

        # početne brzine
        self.vx0 = v0 * np.cos(self.angle)
        self.vy0 = v0 * np.sin(self.angle)

    def simulate(self, dt):  #dt je vremenski korak Eulerove metode
        x, y = 0.0, 0.0 #Početni položaj: projektil kreće iz ishodišta (0,0)
        vx, vy = self.vx0, self.vy0 #Postavljamo trenutne brzine na početne komponente brzine

        xs, ys = [x], [y]
        #Kreiramo liste za spremanje putanje: xs – sve x-koordinate i ys – sve y-koordinate

        while y >= 0:#Petlja traje dok je projektil iznad tla (y ≥ 0)
            v = np.sqrt(vx**2 + vy**2)#trenutna ukupna brzina
            #Treba nam za silu otpora zraka, jer ona ovisi o brzini

            # sile
            Fx = -self.otpor * v * vx
            Fy = -self.otpor * v * vy - self.m * self.g

            # ubrzanja računamo iz sila, iz običnog Newtonovog zakona
            ax = Fx / self.m
            ay = Fy / self.m

            # Euler
            vx += ax * dt #𝑣x(t+dt)=vx(t)+ax(t)dt
            vy += ay * dt
            x += vx * dt #x(t+dt)=x(t)+vx(t+dt)dt
            y += vy * dt

            xs.append(x)
            ys.append(y)
        return xs,ys

# testiranje različitih dt
proj = Projectile(v0=50, angle=45)
dt_vrijednosti = [1.3, 0.1, 0.05, 0.01]
#veći dt - brže,ali manje precizno
#manji dt - sporije,ali fizički realnija putanja

plt.figure()

for dt in dt_vrijednosti: #Iterira kroz sve vrijednosti vremenskog koraka
    xs, ys = proj.simulate(dt)
    #Za svaki dt pozivamo simulate(dt) i dobijemo putanju (x(t), y(t))
    plt.plot(xs, ys, label=f"dt={dt}")

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Kosi hitac s otporom zraka – Eulerova metoda")
plt.legend()
plt.grid()
plt.show()
