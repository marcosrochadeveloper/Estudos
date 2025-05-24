#15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
#salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
#por hora trabalhada.

diasTrabalhados = int(input('Quantos dias o funcionário trabalhou esse mês? '))
print(f'Seu salário será de R${diasTrabalhados*(25*8):.2f}')