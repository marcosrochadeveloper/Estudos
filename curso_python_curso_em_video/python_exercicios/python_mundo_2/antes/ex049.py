# Ex049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número para ver sua tabuada: 8
# 8 x  1 = 8
# 8 x  2 = 16
# 8 x  3 = 24
# 8 x  4 = 32
# 8 x  5 = 40
# 8 x  6 = 48
# 8 x  7 = 56
# 8 x  8 = 64
# 8 x  9 = 72
# 8 x 10 = 80

número = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print(f'{número} x {c:2} = {número*c}')
