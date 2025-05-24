# Ex012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é o preço do produto? R$1000
# O produto que custava R$1000.00, na promoção com desconto de 5% vai custar R$950.00

<<<<<<< Updated upstream
preco = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco-preco*0.05:.2f}')
=======
preço = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava \033[33mR${preço:.2f}\033[m, na promoção com desconto de 5% vai custar \033[33mR${preço-preço*0.05:.2f}\033[m')
>>>>>>> Stashed changes
