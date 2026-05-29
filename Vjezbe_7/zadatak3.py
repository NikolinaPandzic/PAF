import numpy as np

np.random.seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

def medijan(podaci):
    x = sorted(podaci)
    n = len(x)

    if n % 2 == 1:
        return x[n//2]
    else:
        return (x[n//2 - 1] + x[n//2]) / 2

# test
a = [3,1,4,1,5,9,2,6]
b = [3,1,4,1,5,9,2,6,5]

print("\nTest medijana:")
print("a:", medijan(a))
print("b:", medijan(b))

print("\nMedijan mase (ručno):", medijan(mase))
print("Medijan mase (numpy):", np.median(mase))