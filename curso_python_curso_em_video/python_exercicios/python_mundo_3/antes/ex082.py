lista = []
pares = []
ímpares = []
while True:
    número = int(input('Digite um número: '))
    lista.append(número)
    if número%2 == 0:
        pares.append(número)
    else:
        ímpares.append(número)
    continuar = str(input('Quer continuar? ')).upper()
    if continuar == 'N':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')