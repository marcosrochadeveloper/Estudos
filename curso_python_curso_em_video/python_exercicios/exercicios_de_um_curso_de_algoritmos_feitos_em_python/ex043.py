#43) Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1,
#marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
#30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...

c = 30
while c >= 1:
    if c%4 != 0:
        print(c, end=' ')
    else:
        print(f'\033[33m[{c}]\033[m', end=' ')
    c -= 1