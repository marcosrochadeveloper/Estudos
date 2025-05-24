# 74) Crie um programa que preencha automaticamente(usando lógica, não apenas atribuindo diretamente)
# um vetor numérico com 10 posições, conforme abaixo:
# 5 3 5 3 5 3 5 3 5 3
# 0 1 2 3 4 5 6 7 8 9

vetor = []
for c in range(10):
    if c%2 == 0:
        vetor.append(5)
    else:
        vetor.append(3)
print(vetor)