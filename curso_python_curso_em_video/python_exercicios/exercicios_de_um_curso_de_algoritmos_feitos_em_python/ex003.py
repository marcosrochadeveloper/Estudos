#3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
#Ex:
#Nome do Funcionário: Maria do Carmo
#Salário: 1850.45
#O funcionário Maria do Carmo tem um salário de R$1850.45 em Junho.

nome = str(input('Nome do funcionário: '))
salário = float(input('Salário: '))
mês = str(input('Mês: '))
print(f'O funcionário {nome} tem um salário de R${salário:.2f} em {mês}.')