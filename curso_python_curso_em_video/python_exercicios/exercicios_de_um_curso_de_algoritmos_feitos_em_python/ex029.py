#29) Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa
#e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
#- Até 3 anos de empresa: aumento de 3%
#- Entre 3 e 10 anos: aumento de 12.5%
# 10 anos ou mais: aumento de 20%

nome = str(input('Nome do funcionário: '))
salario = float(input('Salário atual: R$'))
tempo = int(input('Quantos anos trabalha na empresa? '))

if tempo < 3:
    aumento = 0.03
elif tempo < 10:
    aumento = 0.125
else:
    aumento = 0.20

print(f'O funcionário {nome} trabalha na empresa a {tempo} anos, por isso ele vai receber um aumento de {aumento*100}% \n'
      f'seu salário atualmente é R${salario:.2f} com o aumento passará a ser R${salario+(salario*aumento):.2f}')