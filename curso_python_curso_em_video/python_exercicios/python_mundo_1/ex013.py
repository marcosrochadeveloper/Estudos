# Ex013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é o salário do Funcionário? R$2000
# Um funcionário que ganhava R$2000.00, com 15% de aumento, passa a receber R$2300.00

<<<<<<< Updated upstream
salario = float(input('Qual é o salário do Funcionário? R$'))
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario+salario*0.15:.2f}')
=======
salário = float(input('Qual é o salário do Funcionário? R$'))
print(f'Um funcionário que ganhava \033[33mR${salário:.2f}\033[m, com \033[33m15%\033[m de aumento, passa a receber \033[33mR${salário+salário*0.15:.2f}\033[m')
>>>>>>> Stashed changes
