lista = list()
for c in range(5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-'*30)
print(f'Você digitou os valores {lista}')
maior = menor = 0
posmaior = []
posmenor = []
for número in lista:
    if menor == 0 or número < menor:
        menor = número
    if número > maior:
        maior = número
for cont, item in enumerate(lista):
    if item == maior:
        posmaior.append(cont)
    if item == menor:
        posmenor.append(cont)

print(f'O maior valor digitado foi {maior} nas posições',end=' ')
for c in range(0,len(posmaior)):
    print(posmaior[c],end='... ')
print('')
print(f'O menor valor digitado foi {menor} nas posições',end=' ')
for c in range(0,len(posmenor)):
    print(posmenor[c],end='... ')
print('')