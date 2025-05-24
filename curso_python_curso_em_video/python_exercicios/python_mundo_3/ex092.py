# Ex092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from datetime import date
anoatual = date.today().year
dados = {
    'Nome': str(input('Nome: ')),
    'Idade': anoatual - int(input('Ano de Nascimento: ')),
    'CTPS': int(input('Carteira de Trabalho (0 não tem): '))}
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = f'{float(input('Salário: R$')):.2f}'
    dados['Aposentadoria'] = dados['Idade'] + (35-(anoatual - dados['Contratação']))
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

