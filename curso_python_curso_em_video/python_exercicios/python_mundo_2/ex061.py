# Ex061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Gerador de PA
# -=-=-=-=-=-=-=-=-=-=
# Primeiro termo: 1
# Razão da PA: 5
# 1 → 6 → 11 → 16 → 21 → 26 → 31 → 36 → 41 → 46 → FIM

print('Gerador de PA')
print('-='*10)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(termo1, end = ' → ')
    termo1 += razao
    c += 1
print('FIM')