#46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.

c = 6
total = 0
while c < 101:
#   print(f'{total} + {c} = {total+c}')
    total += c
    c += 2
print(f'O resultado final foi {total}')