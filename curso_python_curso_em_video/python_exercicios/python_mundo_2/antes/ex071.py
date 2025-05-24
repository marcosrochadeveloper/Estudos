# Ex071 - Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ==============================
#           BANCO CEV
# ==============================
# Que valor você quer sacar? R$25846
# Total de 516 cédulas de R$50.00
# Total de 2 cédulas de R$20.00
# Total de 6 cédulas de R$1.00
# ==============================
# Volte sempre ao BANCO CEV! Tenha um bom dia!

print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30)
sacar = float(input('Que valor você quer sacar? R$'))
cédulas = int(sacar // 50), int((sacar % 50) // 20), int(((sacar % 50) % 20) // 10), int(((sacar % 50) % 20) % 10)
valorescédulas = [50, 20, 10, 1]
for c in range(0,4):
    if cédulas[c] != 0:
        print(f'Total de {cédulas[c]} cédulas de R${valorescédulas[c]}.00')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')