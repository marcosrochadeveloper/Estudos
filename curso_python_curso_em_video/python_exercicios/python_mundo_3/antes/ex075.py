números = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {números}')
print(f'O valor 9 apareceu {números.count(9)} vezes')
if 3 in números:
    print(f'O valor 3 apareceu na {números.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu em nenhuma posição')
print(f'Os valores pares digitados foram ',end = '')
for c in números:
    if c%2 == 0:
        print(c,end=' ')