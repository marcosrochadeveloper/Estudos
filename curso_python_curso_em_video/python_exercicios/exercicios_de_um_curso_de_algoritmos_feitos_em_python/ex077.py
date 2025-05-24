# 77) Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor.
# No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados.

vetor = []
for c in range(7):
    vetor.append(input(f'Informe o nome da {c+1}ª pessoa: '))
vetor.reverse()
print(vetor)