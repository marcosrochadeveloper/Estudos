# 65) Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
# 100 90 80 70 60 50 40 30 20 10 0 Acabou!
i = 100
for c in range(11):
    print(i, end=' ')
    i -= 10
print('Acabou!')