# Ex070 - Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# -----------------------------------
#       LOJA SUPER BARATÃO
# -----------------------------------
# Nome do Produto: Tesoura
# Preço: R$10
#
# Quer continuar? [S/N] s
#
# Nome do Produto: Computador
# Preço: R$1500
#
# Quer continuar? [S/N] n
#
# ----------- FIM DO PROGRAMA ------------
# O total da compra foi R$1510.00
# Temos 1 produtos custando mais de R$1000.00
# O produto mais barato foi Tesoura que custa R$10.00

total = maisde1000 = maisbarato = 0
print('-'*35)
print(f'{'LOJA SUPER BARATÃO':^30}')
print('-'*35)
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        maisde1000 += 1
    if maisbarato == 0 or maisbarato > preço:
        maisbarato = preço
        produtomaisbarato = produto
    print('')
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    print('')
    if continuar == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisde1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtomaisbarato} que custa R${maisbarato:.2f}')