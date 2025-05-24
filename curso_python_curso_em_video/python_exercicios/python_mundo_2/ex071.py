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
valor = float(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
tot_cedulas = 0
while True:
    if cedula <= total:
        tot_cedulas += 1
        total -= cedula
    elif cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    else:
        break
    if cedula > total:
        if tot_cedulas != 0:
            print(f'Total de {tot_cedulas} cédulas de R${cedula:.2f}')
        tot_cedulas = 0
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


# print('='*30)
# print(f'{'BANCO CEV':^30}')
# print('='*30)
# valor = float(input('Que valor você quer sacar? R$'))
# cinquenta = int(valor//50)
# vinte = int((valor%50)//20)
# dez = int(((valor%50)%20)//10)
# um = int(((valor%50)%20)%10)
# if cinquenta != 0:
#     print(f'Total de {cinquenta} cédulas de R$50.00')
# if vinte != 0:
#     print(f'Total de {vinte} cédulas de R$20.00')
# if dez != 0:
#     print(f'Total de {dez} cédulas de R$10.00')
# if um != 0:
#     print(f'Total de {um} cédulas de R$1.00')
# print('='*30)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
