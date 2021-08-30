def maior_primo(n):
    num = 0
    while num <= n:
        num = num + 1
        div = num % 2
        if div == 1:
            return num
        else:
            num = num + 1
