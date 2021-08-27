seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))

hrs = seg // 60**2

hrs_f = hrs % 24

segs = seg % 60

segs2 = seg % 60**2 #resultados em minutos com os segundos

minn = segs2 // 60

dias = hrs // 24

print(dias, "dias,", hrs_f, "horas,", minn, "minutos e", segs, "segundos")

