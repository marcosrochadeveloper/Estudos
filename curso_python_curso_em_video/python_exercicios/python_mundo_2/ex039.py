# Ex039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# OBS: No exemplo abaixo também tem a função de verificar o sexo da pessoa que está se alistando, para ser uma prática mais completa.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Ano de nascimento: 2015
# Qual o seu sexo? [M] [F] m
# Quem nasceu em 2015 tem 10 anos em 2025.
# Você ainda não tem 18 anos. Ainda faltam 8 anos para o seu alistamento.
# Seu alistamento será em 2033.
# ---------------------------------------
# Ano de nascimento: 2007
# Qual o seu sexo? [M] [F] m
# Quem nasceu em 2007 tem 18 anos em 2025.
# Você tem que se alistar IMEDIATAMENTE!
# ---------------------------------------
# Ano de nascimento: 1998
# Qual o seu sexo? [M] [F] m
# Quem nasceu em 1998 tem 27 anos em 2025.
# Você já deveria ter se alistado há 9 anos.
# Seu alistamento foi em 2016.
# ---------------------------------------
# Ano de nascimento: 2007
# Qual o seu sexo? [M] [F] f
# Quem nasceu em 2007 tem 18 anos em 2025.
# Você tem 18 anos, mas por ser mulher, não tem obrigação de se alistar!
from datetime import date
anoatual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoatual - nascimento
sexo = str(input('Qual o seu sexo? [M] [F]: ').upper())
print(f'Quem nasceu em {nascimento} tem {idade} anos em {anoatual}.')
if sexo == 'F':
    print(f'Você tem {idade} anos, mas por ser mulher, não tem obrigação de se alistar!')
elif idade < 18:
    print(f'Você ainda não tem 18 anos! Ainda faltam {18-idade} anos para o seu alistamento.')
    print(f'Seu alistamento será em {18 - idade + anoatual}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {anoatual - (idade-18)}.')