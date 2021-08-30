lar = int(input('Digite a largura: '))
alt = int(input('Digite a altura: '))
lin = 1

while alt > 0:
    print('#' * lar)
    while lin < alt - 1:
        print('#' + ' ' * (lar - 2) + '#')
        lin += 1
    print('#' * lar)
    alt = 0
