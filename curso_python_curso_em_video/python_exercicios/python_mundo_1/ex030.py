# Ex030 - Crie um programa que leia um número inteiro, e mostre na tela se ele é par ou ímpar.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 5
# O número 5 é ímpar

# --------------------------------------------------------------

# Digite um número: 12
# O número 12 é par

<<<<<<< Updated upstream
num = int(input('Digite um número: '))
print(f"O número {num} é par") if num%2 == 0 else print(f'O Número {num} é ímpar')
=======
numero = int(input('Digite um número: '))
if numero%2 == 0:
    print(f'O número \033[33m{numero}\033[m é par')
else:
    print(f'O número \033[33m{numero}\033[m é ímpar')
>>>>>>> Stashed changes
