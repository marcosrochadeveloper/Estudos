from random import sample
#range(10) - valores entre 0 e 9 e o número 5 é o número de elementos aleatórios a serem sorteados
valores = sample(range(10), 5)
print(f'Os valores sorteados foram: ',end='')
sorted(valores)
for c in valores:
    print(c, end=' ')
print('')
valores = sorted(valores)
#A referência [-1] mostra o último elemento da variável.
print(f'O maior valor sorteado foi {valores[-1]}')
print(f'O menor valor sorteado foi {valores[0]}')