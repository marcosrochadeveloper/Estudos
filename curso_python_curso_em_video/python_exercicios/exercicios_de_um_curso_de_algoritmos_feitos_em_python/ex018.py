#18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.

from datetime import datetime
anoAtual = datetime.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = anoAtual-nascimento
print(f'Por ter nascido no ano {nascimento} você tem ou vai fazer esse ano {idade} anos de idade!')
if idade < 16:
    print('Você ainda não pode votar!')
elif idade < 18:
    print('Você já pode votar, mas não é obrigatório!')
else:
    print('Você tem a obrigação de votar!')