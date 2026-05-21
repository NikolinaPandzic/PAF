import numpy as np

malo_n = np.array([99.8, 100.1, 99.9, 100.2, 100.0])

np.random.seed(42) 
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000)

def sigma_n(x):
    return np.sqrt(np.sum((x - np.mean(x))**2) / len(x))

def s(x):
    return np.sqrt(np.sum((x - np.mean(x))**2) / (len(x) - 1))

def sigma_xbar(x):
    return s(x) / np.sqrt(len(x))

for naziv, data in [("malo_n", malo_n), ("veliko_n", veliko_n)]:
    print(f"\nSkup: {naziv}")
    print(f"sigma_n = {sigma_n(data):.5f}")
    print(f"s = {s(data):.5f}")
    print(f"sigma_xbar = {sigma_xbar(data):.5f}")

print("ODGOVORI:") 
print("(a) s ~ konstantan, sigma_xbar opada s većim n") 
print("(b) razlika velika za mali skup, zanemariva za veliki") 
print("(c) np.std() (dijeli s n) koristi se za populaciju")