# 53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos

idades = []
sexos = []
homens = mulheres = mais20 = idadetotal = idadetotalhomens = 0
for c in range(1, 6):
    idades.append(int(input(f'Idade da {c}ª pessoa: ')))
    sexos.append(str(input(f'Sexo da {c}ª pessoa[M/F]: ').upper()))
    idadetotal += idades[c-1]
    if sexos[c-1] == 'M':
        homens += 1
        idadetotalhomens += idades[c-1]
    elif sexos[c-1] == 'F':
        mulheres += 1
    if idades[c-1] > 20 and sexos[c-1] == 'F':
        mais20 += 1
media = idadetotal / 5
mediahomens = idadetotalhomens / homens
print(f'a) Foram cadastrados {homens} homens!')
print(f'b) Foram cadastradas {mulheres} mulheres!')
print(f'c) A média de idade do grupo é de aproximadamente {int(media)} anos!')
print(f'd) A média de idade dos homens é de aproximadamente {int(mediahomens)} anos!')
print(f'e) {mais20} mulheres tem mais de 20 anos!')