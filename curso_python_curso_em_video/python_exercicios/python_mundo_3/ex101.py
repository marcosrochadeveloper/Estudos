# Ex101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO')

print('-'*30)
ano_nascimento = int(input('Em que ano você nasceu? '))
voto(ano_nascimento)