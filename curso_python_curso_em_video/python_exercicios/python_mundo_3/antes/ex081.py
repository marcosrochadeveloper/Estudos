lista = []
listadecrescente = []
total = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    total += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
lista.sort()
for c in range(len(lista)):
    listadecrescente.append(lista[len(lista)-c-1])
#lista.reverse() - Só isso já colocaria em ordem decrescente!
print('-='*30)
print(f'Você digitou {total} elementos.')
print(f'Os valores em ordem crescente são {lista}')
print(f'Os valores em ordem decrescente são {listadecrescente}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')