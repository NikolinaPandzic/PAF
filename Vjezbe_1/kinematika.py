import matplotlib.pyplot as plt

def jednoliko_gibanje(m, F, t_max, dt=0.1):
    a = F / m
    # Početne vrijednosti
    t = 0
    v = 0
    x = 0

    # Liste za grafove
    t_lista = []
    x_lista = []
    v_lista = []
    a_lista = []

    # Simulacija gibanja
    while t <= t_max:
        t_lista.append(t)
        x_lista.append(x)
        v_lista.append(v)
        a_lista.append(a)

        v = v + a * dt
        x = x + v * dt
        t = t + dt

    # x-t graf
    plt.figure()
    plt.plot(t_lista, x_lista, 'b')
    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.title("x - t graf")
    plt.grid(True)

    # v-t graf
    plt.figure()
    plt.plot(t_lista, v_lista, 'r')
    plt.xlabel("t (s)")
    plt.ylabel("v (m/s)")
    plt.title("v - t graf")
    plt.grid(True)

    # a-t graf
    plt.figure()
    plt.plot(t_lista, a_lista, 'g')
    plt.xlabel("t (s)")
    plt.ylabel("a (m/s^2)")
    plt.title("a - t graf")
    plt.grid(True)

    plt.show()
