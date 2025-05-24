# 64) Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
# 0 5 10 15 20 25 30 35 40 Acabou!
i = 0
for c in range(9):
    print(i, end=' ')
    i += 5
print('Acabou!')