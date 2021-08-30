n = int(input('Digite um número inteiro > 0: '))


def e_primo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator < x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True


while n > 0:
    if e_primo(n):
        print(n, 'É primo!')
    else:
        print(n, 'Não é primo :-(')
    n = int(input('Digite um número inteiro: '))
