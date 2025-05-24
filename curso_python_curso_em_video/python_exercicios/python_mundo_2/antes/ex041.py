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


from datetime import datetime
anoatual = datetime.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = anoatual - nascimento
if idade > 25:
    classificação = 'MASTER'
elif idade > 19:
    classificação = 'SÊNIOR'
elif idade > 14:
    classificação = 'JUNIOR'
elif idade > 9:
    classificação = 'INFANTIL'
else:
    classificação = 'MIRIM'
print(f'O atleta tem {idade} anos.')
print(f'Classificação: {classificação}')