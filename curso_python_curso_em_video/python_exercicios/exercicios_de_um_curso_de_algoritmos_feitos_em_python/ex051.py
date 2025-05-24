# 51) Faça um aplicativo que leia o preço de 8 produtos.
# No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.

produtos = []
while True:
    produtos.append(float(input(f'Informe o {len(produtos)+1}º preço: R$')))
    if len(produtos) == 8:
        break
menor = maior = produtos[0]
for produto in produtos:
    if produto > maior:
        maior = produto
    if produto < menor:
        menor = produto
print(f'O maior preço informado foi R${maior:.2f}!')
print(f'O menor preço informado foi R${menor:.2f}!')