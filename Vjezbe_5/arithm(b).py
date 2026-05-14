import statistics

x = []

for i in range(10):
    broj = float(input(f"Unesi broj {i+1}: "))
    x.append(broj)

# gotove funkcije
sredina = statistics.mean(x)
devijacija = statistics.stdev(x)

print("Aritmetička sredina:", sredina)
print("Standardna devijacija:", devijacija)