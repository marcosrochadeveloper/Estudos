#33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = int(input('Em quantos anos você quer pagar o empréstimo? '))
prestacao = valor / (tempo*12)
if prestacao <= salario*0.3:
    print(f'Empréstimo aprovado! Você terá que pagar {tempo*12} parcelas de R${prestacao:.2f}')
else:
    print(f'EMPRÉSTIMO NEGADO!')