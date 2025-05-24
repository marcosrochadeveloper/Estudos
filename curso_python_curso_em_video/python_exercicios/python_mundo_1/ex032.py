# Ex032 - Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO.
# |||DICAS|||
# Todoo ano bissexto é Múltiplo de 4
# Se for múltiplo de 100 precisa ser também múltiplo de 400
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Que ano quer analisar? Coloque 0 para analisar o ano atual: 1900
# O ano 1900 não é bissexto!

# ---------------------------------------------------------------------

# Que ano quer analisar? Coloque 0 para analisar o ano atual: 2016
# O ano 2016 é bissexto!

# ----------------------------------------------------------------------

# Que ano quer analisar? Coloque 0 para analisar o ano atual: 0
# O ano 2025 não é bissexto!

<<<<<<< Updated upstream
from datetime import date
anoatual = date.today().year
=======
from datetime import datetime
>>>>>>> Stashed changes
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = anoatual

if ano % 4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto')