print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
preços = ('Lápis', 1.75,
          'Borracha', 2.00,
          'Caderno', 15.90,
          'Estojo', 25.00,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90,)
for c in range(len(preços)):
    if c%2 == 0:
        print(f'{preços[c]:.<30} R$',end='')
    else:
        print(f'{preços[c]:>7.2f}')
print('-'*40)