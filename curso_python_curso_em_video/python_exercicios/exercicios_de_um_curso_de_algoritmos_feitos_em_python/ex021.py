#21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.

from datetime import datetime
ano_atual = datetime.today().year
ano = int(input('Digite um ano [0] para o ano atual: '))
if ano == 0:
    ano = ano_atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO')