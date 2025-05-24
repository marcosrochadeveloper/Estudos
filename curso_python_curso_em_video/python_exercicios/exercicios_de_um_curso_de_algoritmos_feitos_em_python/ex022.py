# 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.

from datetime import datetime
ano_atual = datetime.today().year
ano_nascimento = int(input('Qual o ano de nascimento? '))
idade = ano_atual - ano_nascimento
if idade < 18:
    print(f'Você tem {idade} anos, falta(m) {18-idade} ano(s) para você se alistar!')
elif idade == 18:
    print(f'Você tem 18 anos, e está no ano do seu alistamento!')
else:
    print(f'Você tem {idade} anos, faz(em) {idade-18} ano(s) desde o seu alistamento!')