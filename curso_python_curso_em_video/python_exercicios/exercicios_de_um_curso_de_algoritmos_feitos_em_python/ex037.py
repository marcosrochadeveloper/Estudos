#37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores.
# Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
#No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%

# - Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%
salario_atual = float(input('Informe o salário atual do funcionário: R$'))
anos = int(input('Faz quantos anos que esse funcionário trabalha na empresa? '))
genero = str(input('Informe o gênero do funcionário [M/F]: ')).upper()
print(genero)
if genero != 'M' and genero != 'F':
    print('[ERRO]: Informe um gênero válido!')
else:
    if genero == 'F':
        if anos < 15:
            aumento = 0.05
        elif anos <= 20:
            aumento = 0.12
        else:
            aumento = 0.23
        print(f'A funcionária que recebia o salário de R${salario_atual:.2f}, por já trabalhar a {anos} anos na empresa, passará a receber R${salario_atual + salario_atual*aumento:.2f} foi recebido um aumento de {aumento*100}%')
    else:
        if anos < 20:
            aumento = 0.03
        elif anos <= 30:
            aumento = 0.13
        else:
            aumento = 0.25
        print(f'O funcionário que recebia o salário de R${salario_atual:.2f}, por já trabalhar a {anos} anos na empresa, passará a receber R${salario_atual + salario_atual*aumento:.2f} foi recebido um aumento de {aumento*100}%')
