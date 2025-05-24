# Ex041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Ano de Nascimento: 2005
# O atleta tem 20 anos.
# Classificação: SÊNIOR

from datetime import date
anoatual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = anoatual - nascimento
if idade < 10: #ATÉ 9 ANOS
    classificacao = 'MIRIM'
elif idade < 15: #ATÉ 14 ANOS
    classificacao = 'INFANTIL'
elif idade < 20: #ATÉ 19 ANOS
    classificacao = 'JUNIOR'
elif idade < 26: #ATÉ 25 ANOS
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'
print(f'O atleta tem {idade} anos.')
print(f'Classificação: {classificacao}')