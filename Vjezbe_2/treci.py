import math
import matplotlib.pyplot as plt
import calculus

def f1(x):
    return x**3

def f2(x):
    return math.sin(x)

def df1(x):
    return 3*x**2

def df2(x):
    return math.cos(x)

a=-2
b=2
vrijednosti_eps=[0.1, 0.01, 0.001]
for eps in vrijednosti_eps:
    xs, ys = calculus.range_derivacije(f1, a, b, eps, 0.1)
    plt.plot(xs, ys, label=f'numericki epsilon={eps}')

xs=[]
ys=[]
x=a
while x <= b:
    xs.append(x)
    ys.append(df1(x))
    x += 0.1
plt.plot(xs, ys, '--', label=f'analiticki')
plt.legend()
plt.title(f'Kubna funkcija')
plt.show()

for eps in vrijednosti_eps:
    xs, ys = calculus.range_derivacije(f2, a, b, eps, 0.1)
    plt.plot(xs, ys, label=f'numericki epsilon={eps}')
xs=[]
ys=[]
x=a
while x <= b:
    xs.append(x)
    ys.append(df2(x))
    x += 0.1
plt.plot(xs, ys, '--', label=f'analiticki')
plt.legend()
plt.title(f'sin(x)')
plt.show()