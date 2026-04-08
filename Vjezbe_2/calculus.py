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