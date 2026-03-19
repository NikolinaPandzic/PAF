while True:
    try:
        unos = input("unesi prvu točku (x y):").split()#uzme korisnički unos i razdvoji ga po razmacima
        x1 = float(unos[0]) #pretvara prvi dio u broj 
        y1 = float(unos[1])
        break
    except:
        print("Greška, probaj opet")
while True:
    try:
        unos = input("unesi drugu točku (x y):").split()
        x2 = float(unos[0])
        y2 = float(unos[1])
        break
    except:
        print("Greška,probaj opet")
if x1 == x2:
    print("x = ",x1," pravac okomit na x os")#ako su x koordinate jednake pravac ima jednadžbu x=K
else:
    k = (y2 - y1) / (x2 - x1) #nagib pravca
    l = y1 - k*x1             #odsječak na y osi
    print("y= ",k,"x+",l)