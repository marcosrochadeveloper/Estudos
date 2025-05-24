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
# Você ainda não tem 18 anos. Ainda faltam 8 anos para o alistamento.
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

from datetime import datetime
anoatual = datetime.today().year
nascimento = int(input('Ano de nascimento: '))
sexo = str(input('Qual o seu sexo? [M] [F] ')).lower()
idade = anoatual - nascimento
print(f'Quem nasceu em \033[33m{nascimento}\033[m tem \033[33m{idade}\033[m anos em \033[33m{anoatual}\033[m.')
if sexo == 'm':
    if idade < 18:
        if 18-idade != 1:
            print(f'Você ainda não tem 18 anos. Ainda faltam \033[33m{18-idade}\033[m anos para o alistamento.')
        else:
            print(f'Você ainda não tem 18 anos. Ainda falta \033[33m{18-idade}\033[m ano para o alistamento.')
        print(f'Seu alistamento será em \033[33m{anoatual+(18-idade)}\033[m.')
    elif idade == 18:
        print('Você tem que se alistar \033[33mIMEDIATAMENTE\033[m!')
    else:
        print(f'Você já deveria ter se alistado há \033[33m{idade-18}\033[m anos.')
        print(f'Seu alistamento foi em \033[33m{anoatual-(idade-18)}\033[m.')
elif sexo == 'f':
    print(f'Você tem {idade} anos, mas por ser mulher, não tem obrigação de se alistar!')
else:
    print('Informe um valor de sexo VÁLIDO!')