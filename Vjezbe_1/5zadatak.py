import matplotlib.pyplot as plt

def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        print("Jednadžba pravca: x =", x1)
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print("Jednadžba pravca: y =", round(k, 2), "x +", round(l, 2))
    plt.plot([x1, x2], [y1, y2])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pravac kroz dvije točke')
    plt.grid(True)
    plt.scatter([x1, x2], [y1, y2])

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

jednadzba_pravca(x1, y1, x2, y2)
opcija = input("prikaz ili spremi: ")

if opcija == "spremi":
    ime = input("ime datoteke (npr. graf.pdf): ")
    plt.savefig(ime)
else:
    plt.show()