# Ex047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 Acabou

for c in range(2,52,2):
    print(c, end=' ')
print('Acabou')

'''for c in range(1,51):
    if c%2 == 0:
        print(c, end=' ')
print('Acabou')'''