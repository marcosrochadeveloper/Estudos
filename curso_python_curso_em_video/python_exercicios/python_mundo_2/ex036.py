# Ex036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
# Valor da casa: R$80000
# Salário do comprador: R$1600
# Quantos anos de financiamento? 7
# Para pagar uma casa de R$80000.00 em 7 anos a prestação será de R$952.38
# Empréstimo NEGADO!
#
# -------------------------------------------------------
#
# Valor da casa: R$80000
# Salário do comprador: R$10000
# Quantos anos de financiamento? 7
# Para pagar uma casa de R$80000.00 em 7 anos a prestação será de R$952.38
# Empréstimo pode ser CONCEDIDO!

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12) #(anos * 12) mostrará a quantidade de mêses
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos serão {anos*12} prestações de R${prestacao:.2f}')
if salario * 0.3 > prestacao:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')