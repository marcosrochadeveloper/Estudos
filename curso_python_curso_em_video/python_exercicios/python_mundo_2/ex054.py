# Ex054 - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# OBS: O EXEMPLO ABAIXO É BASEADO NO ANO DE 2025
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Em que ano a 1ª pessoa nasceu? 1998
# Em que ano a 2ª pessoa nasceu? 2005
# Em que ano a 3ª pessoa nasceu? 2015
# Em que ano a 4ª pessoa nasceu? 2013
# Em que ano a 5ª pessoa nasceu? 2011
# Em que ano a 6ª pessoa nasceu? 2010
# Em que ano a 7ª pessoa nasceu? 1980
# No total tivemos 3 pessoas maiores de idade
# E também tivemos 4 pessoas menores de idade

from datetime import date
ano_atual = date.today().year
maiores = menores = 0
for c in range(1,8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print(f'''No total tivemos {maiores} pessoas maiores de idade
E também tivemos {menores} pessoas menores de idade''')
