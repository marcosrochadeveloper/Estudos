#47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0

c = 500
total = 0
while c >= 0:
#   print(f'{total} + {c} = {total+c}')
    total += c
    c -= 50
print(f'O resultado final foi {total}')