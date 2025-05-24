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

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*25)
    for c in range(1,11):
        print(f'{num} x {c:>2} = {num*c}')
    print('-'*25)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')