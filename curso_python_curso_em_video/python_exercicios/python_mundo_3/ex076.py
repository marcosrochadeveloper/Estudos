# Ex076 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#

print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
precos = ('Lápis', 1.75,
          'Borracha', 2.00,
          'Caderno', 15.90,
          'Estojo', 25.00,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90)
for c, item in enumerate(precos):
    if c%2 == 0:
        print(f'{item:.<30}R$', end =' ')
    else:
        print(f'{item:>6.2f}')
print('-'*40)