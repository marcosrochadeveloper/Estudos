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

print('-'*30)
print(f'{'LOJA SUPER BARATÃO':^30}')
print('-'*30)
preco_mais_barato = mais_de_1000 = total = 0
nome_mais_barato = ''
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        mais_de_1000 += 1
    if preco_mais_barato == 0 or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome
    continuar = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while continuar not in 'SN':
        continuar = str(input('Resposta Inválida! Quer continuar? [S/N]: ').strip().upper()[0])
    if continuar == 'N':
        break

print(f'{' FIM DO PROGRAMA ':-^30}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais_de_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${preco_mais_barato:.2f}')