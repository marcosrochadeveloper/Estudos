# Ex054 - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
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
pessoas = []
idades = []
maiores = 0
menores = 0
anoatual = date.today().year
for c in range (1,8):
    pessoas.append(int(input(f'Em que ano a {c}ª pessoa nasceu? ')))
    idades.append(anoatual-pessoas[c-1])
    if idades[c-1] >= 18:
        maiores += 1
    else:
        menores += 1
print(f'No total tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')