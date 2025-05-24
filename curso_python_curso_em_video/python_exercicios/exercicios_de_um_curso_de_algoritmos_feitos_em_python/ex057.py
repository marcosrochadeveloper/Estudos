# 57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
# No final, mostre o total de salários pagos aos homens e o total pago às mulheres.
# O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um funcionário.

total_homens = total_mulheres = salario_homens = salario_mulheres = 0
while True:
    salario = float(input('Qual o salário do funcionário? R$'))
    sexo = str(input('Qual o sexo do funcionário? [M/F]').upper())
    if sexo == 'M':
        total_homens += 1
        salario_homens += salario
    else:
        total_mulheres += 1
        salario_mulheres += salario
    continuar = str(input('Quer continuar? [S/N]').upper())
    if continuar == 'N':
        break
print(f'Somando os salários dos {total_homens} homens informados, ficou um total de R${salario_homens:.2f}!')
print(f'Somando os salários das {total_mulheres} mulheres informadas, ficou um total de R${salario_mulheres:.2f}!')