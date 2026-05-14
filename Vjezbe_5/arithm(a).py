n = 10
x = []

for i in range(n):
    broj = float(input(f"Unesi broj {i+1}: "))
    x.append(broj)

# aritmetička sredina
suma = 0
for broj in x:
    suma += broj

ar_sredina = suma / n

# standardna devijacija
suma_kv = 0
for broj in x:
    suma_kv += (broj - ar_sredina) ** 2

sigma = (suma_kv / (n * (n - 1))) ** 0.5

print("Aritmetička sredina:", ar_sredina)
print("Standardna devijacija:", sigma)