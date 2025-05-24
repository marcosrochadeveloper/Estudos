# Ex034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é o salário do funcionário? R$900
# Quem ganhava R$900.00 passa a ganhar R$1035.00 agora.
<<<<<<< Updated upstream

#------------------------------------------------------------------

=======
>>>>>>> Stashed changes
# Qual é o salário do funcionário? R$9000
# Quem ganhava R$9000.00 passa a ganhar R$9900.00 agora.

salario = float(input('Qual é o salário do funcionário? R$'))
<<<<<<< Updated upstream
novo_salario = salario + (salario*0.1) if salario > 1250 else salario + (salario*0.15)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora')
=======
novosalario = salario + salario * 0.1 if salario > 1250 else salario + salario * 0.15
print(f'Quem ganhava \033[33mR${salario:.2f}\033[m passa a ganhar \033[33mR${novosalario:.2f}\033[m agora.')

>>>>>>> Stashed changes
