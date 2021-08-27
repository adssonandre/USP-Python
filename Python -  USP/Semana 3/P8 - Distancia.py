import math

x1 = float(input("Valor de x1: "))
y1 = float(input("Valor de y1: "))

x2 = float(input("Valor de x2: "))
y2 = float(input("Valor de y2: "))

lenth = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if lenth >= 10:
    print("longe")
else:
    print("perto")
