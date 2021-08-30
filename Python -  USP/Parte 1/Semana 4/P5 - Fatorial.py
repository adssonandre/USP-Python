n = int(input('Digite o valor de n: '))
fat = 1

while n > 0:
    while n > 1:
        fat = fat * n
        n = n - 1
        print(fat)
    n -= 1
