lista = []
while True:
    valor = int((input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
lista.sort()
print('-='*30)
print(f'Você digitou os valores {lista}')