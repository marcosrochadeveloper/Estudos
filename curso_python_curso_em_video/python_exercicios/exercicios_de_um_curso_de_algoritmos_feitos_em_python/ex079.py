# 79) Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.
# No final, mostre quais são os números pares que foram digitados e em que posições eles estão armazenados.
numeros = []
pares = []
posicoes = []
for c in range(10):
    numeros.append((int(input(f'Digite o {c+1}º número inteiro: '))))
    if numeros[c]%2 == 0:
        pares.append(numeros[c])
        posicoes.append(c)
print(f'Os números pares digitados foram {pares}\n'
      f'nas posições {posicoes}')