# Ex067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Quer ver a tabuada de qual valor? 5
# ------------------------------
# 5 x  1 = 5
# 5 x  2 = 10
# 5 x  3 = 15
# 5 x  4 = 20
# 5 x  5 = 25
# 5 x  6 = 30
# 5 x  7 = 35
# 5 x  8 = 40
# 5 x  9 = 45
# 5 x 10 = 50
# ------------------------------
# Quer ver a tabuada de qual valor? -1
# ------------------------------
# PROGRAMA TABUADA ENCERRADO. Volte sempre!

tabuada = int(input('Quer ver a tabuada de qual valor? '))
while True:
    print('-'*30)
    print(f'{tabuada} x  1 = {tabuada*1}')
    print(f'{tabuada} x  2 = {tabuada*2}')
    print(f'{tabuada} x  3 = {tabuada*3}')
    print(f'{tabuada} x  4 = {tabuada*4}')
    print(f'{tabuada} x  5 = {tabuada*5}')
    print(f'{tabuada} x  6 = {tabuada*6}')
    print(f'{tabuada} x  7 = {tabuada*7}')
    print(f'{tabuada} x  8 = {tabuada*8}')
    print(f'{tabuada} x  9 = {tabuada*9}')
    print(f'{tabuada} x 10 = {tabuada*10}')
    print('-'*30)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')