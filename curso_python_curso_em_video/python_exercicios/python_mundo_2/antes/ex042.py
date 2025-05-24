# Ex042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro segmento: 5
# Segundo segmento: 5
# Terceiro segmento: 5
# Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 == seg3:
        tipo = 'EQUILÁTERO'
    elif seg1 != seg2 != seg3 != seg1:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓSCELES'
    print(f'Os segmentos acima \033[33mPODEM FORMAR\033[m um triângulo \033[33m{tipo}\033[m.')
else:
    print('Os segmentos acima \033[33mNÃO PODEM FORMAR\033[m um triângulo.')
