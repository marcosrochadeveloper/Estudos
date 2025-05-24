#41) Desenvolva um programa que mostre na tela a seguinte contagem:
#100 95 90 85 80 ... 0 Acabou!

c = 100
while c >= 0:
    print(c, end=' ')
    c -= 5
print('Acabou!')