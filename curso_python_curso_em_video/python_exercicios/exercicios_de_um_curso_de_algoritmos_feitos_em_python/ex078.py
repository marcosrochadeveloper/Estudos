# 78) Escreva um programa que leia 15 números e guarde-os em um vetor. No final, mostre o vetor inteiro na tela
# e em seguida mostre em que posições foram digitados valores que são múltiplos de 10.

vetor = []
multiplo10 = []
for c in range(15):
    vetor.append(int(input('Digite um número: ')))
    if vetor[c]%10 == 0:
        multiplo10.append(c)
print(vetor)
print(f'Foram digitados números múltiplos de 10 nas posições {multiplo10}')
