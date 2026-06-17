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
 
print("(a) sigma_xbar opada s većim n") #Veći broj mjerenja → manja nesigurnost prosjeka
print("(b) razlika velika za mali skup, zanemariva za veliki")
#Za mali broj mjerenja razlika između σₙ i s je veća jer se dijeljenje s n i n-1 dosta razlikuje.
#Za veliki broj mjerenja razlika je vrlo mala jer su n i n-1 gotovo jednaki. 
print("(c) np.std() (dijeli s n) koristi se za populaciju")
#Ako imamo samo uzorak mjerenja, koristi se dijeljenje s n-1