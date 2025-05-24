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
#

from math import ceil # A FUNÇÃO 'CEIL' ARREDONDA PARA CIMA!

valor = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestação = valor / (tempo*12)

print(f'Para pagar uma casa de \033[33mR${valor:.2f}\033[m em \033[33m{tempo} anos\033[m a prestação será de \033[33mR${prestação:.2f}\033[m')

if prestação < salário*0.3: 
    print('\033[32mEmpréstimo pode ser CONCEDIDO\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')
    print(f'Para ser aprovado e pegar um empréstimo de \033[33mR${valor:.2f}\033[m e pagar em \033[33m{tempo} anos\033[m')
    print(f'você precisaria ter um salário acima de \033[33mR${prestação*100 / 30:.2f}\033[m')
    print(f'Com esse salário de \033[33mR${salário:.2f}\033[m você teria que parcelar para pagar em aproximadamente \033[33m{ceil((valor/(salário*0.3))/12)} anos\033[m')