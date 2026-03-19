def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
        return
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    if l >= 0:
        print(f"Jednadžba pravca: y = {k}x + {l}")
    else:
        print(f"Jednadžba pravca: y = {k}x - {abs(l)}")
x1 = float(input("x1= "))
y1 = float(input("y1= "))
x2 = float(input("x2= "))
y2 = float(input("y2= "))
jednadzba_pravca(x1, y1, x2, y2)