lista = []
for c in range(5):
    valor = int(input('Digite um valor: '))
    pos=0
    while pos >= len(lista):
        if c == 0:
            print('Adicionado ao final da lista...')
            lista.append(valor)
            break
        elif valor < lista[pos]:
            lista.insert(pos, valor)
            print(f'Adicionado na posição {pos}')
            break
        pos+=1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')