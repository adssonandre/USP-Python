n = int(input('Digite um número inteiro: '))
x = 1
d_i = n // x
d = d_i % 10
soma = 0

while d_i != 0:
    print(d)
    soma = soma + d
    x = x * 10
    d_i = n // x
    d = d_i % 10
print('A soma dos dígitos é: ', soma)
