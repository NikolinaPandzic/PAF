import matplotlib.pyplot as plt
F = float(input("Unesi silu (N): "))
m = float(input("Unesi masu (kg): "))

a = F / m
#početne vrijednosti
t = 0
dt = 0.1
v = 0
x = 0

#liste za grafove
t_lista = []
x_lista = []
v_lista = []
a_lista = []
while t <= 10:
    t_lista.append(t)
    x_lista.append(x)
    v_lista.append(v)
    a_lista.append(a)

    v = v + a * dt
    x = x + v * dt
    t = t + dt

#x-t graf
plt.figure()
plt.plot(t_lista, x_lista)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("x - t graf")
plt.grid()

#v-t graf
plt.figure()
plt.plot(t_lista, v_lista)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("v - t graf")
plt.grid()

#a-t graf
plt.figure()
plt.plot(t_lista, a_lista)
plt.xlabel("t (s)")
plt.ylabel("a (m/s^2)")
plt.title("a - t graf")
plt.grid()

plt.show()