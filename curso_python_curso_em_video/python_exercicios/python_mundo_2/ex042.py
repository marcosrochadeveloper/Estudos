# Ex042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes
# DICA: CADA LADO DO TRIÂNGULO NÃO PODE SER MAIOR QUE A SOMA DOS OUTROS DOIS
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro segmento: 5
# Segundo segmento: 5
# Terceiro segmento: 5
# Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 == seg2 == seg3:
    triangulo = 'EQUILÁTERO'
elif seg1 != seg2 != seg3 != seg1:
    triangulo = 'ESCALENO'
else:
    triangulo = 'ISÓSCELES'

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo {triangulo}.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')