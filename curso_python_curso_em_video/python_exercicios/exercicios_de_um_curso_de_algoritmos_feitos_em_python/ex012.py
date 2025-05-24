#12) Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

preço = float(input('Qual o preço do produto? R$'))
print(f'Na promoção com 5% de desconto o produto que custava R${preço:.2f} ficou por R${preço-(preço*0.05):.2f}')