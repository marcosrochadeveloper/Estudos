# Ex035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#         Analisador de Triângulos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Primeiro segmento: 3.5
# Segundo segmento: 2.75
# Terceiro segmento: 4
# Os segmentos acima PODEM FORMAR um triângulo!

# ------------------------------------------------------------

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#         Analisador de Triângulos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Primeiro segmento: 2
# Segundo segmento: 4
# Terceiro segmento: 9
# Os segmentos acima NÃO PODEM FORMAR um triângulo!

<<<<<<< Updated upstream
#DICA: CADA LADO DO TRIÂNGULO NÃO PODE SER MAIOR QUE A SOMA DOS OUTROS DOIS

print('-='*20)
print(f'{'Analisador de Triângulos':^40}')
print('-='*20)
segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Primeiro segmento: '))
triangulo = 'NÃO PODEM FORMAR'
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    triangulo = 'PODEM FORMAR'
print(f'Os segmentos acima {triangulo} um triângulo!')
=======
print(f'\033[33m{'-='*20}\033[m')
print('        Analisador de Triângulos')
print(f'\033[33m{'-='*20}\033[m')
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('\033[32mOs segmentos acima PODEM FORMAR um triângulo!\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR um triângulo!\033[m')
>>>>>>> Stashed changes
