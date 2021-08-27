import math

a = float(input("Constante a = "))
b = float(input("Constante b = "))
c = float(input("Constante c = "))

delt = b ** 2 - 4 * a * c

if delt < 0:
	print("esta equação não possui raízes reais")
else:
	raiz1 = (-b + math.sqrt(delt)) / (2 * a)
	raiz2 = (-b - math.sqrt(delt)) / (2 * a)
	if delt == 0:
		print("a raiz desta equação é", raiz1)
	else:
		if raiz1 < raiz2:
			print("as raízes da equação são", raiz1,"e", raiz2)
		else:
			print("as raízes da equação são", raiz2,"e", raiz1)


