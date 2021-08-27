num = int(input("Digite um número: "))

div = num % 5

div2 = num % 3

if div == 0 and div2 == 0:
    print("FizzBuzz")
else:
    print(num)

