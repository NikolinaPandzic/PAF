import math

def derivacija(f, x, eps=0.001, metoda="three-step"):
    if metoda == "two-step":
        return (f(x+eps)-f(x))/eps
    else:
        return (f(x+eps)-f(x-eps))/(2*eps)
    
def range_derivacije(f, a, b, eps=0.001, step=0.1, metoda="three-step"):
    xs=[]
    ys=[]
    x=a
    while x <= b:
        xs.append(x)
        ys.append(derivacija(f, x, eps, metoda))
        x += step
    return xs, ys

def pravokutna_aproksimacija(f, a, b, n):
    dx=(b-a)/n
    donja_suma=0
    gornja_suma=0
    x=a
    for i in range(n):
        donja_suma += f(x)
        gornja_suma += f(x+dx)
        x += dx
    return donja_suma*dx, gornja_suma*dx

def trapezna_metoda(f, a, b, n):
    dx=(b-a)/n
    suma=0
    x=a
    for i in range(n):
        suma += (f(x)+f(x+dx))/2
        x += dx
    return suma*dx
