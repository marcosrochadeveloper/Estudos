# Ex003 - Crie um programa que leia dois números e mostre a soma entre eles.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 10
# Digite outro número: 15
# A soma de 10 + 15 é igual a 25

<<<<<<< Updated upstream
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print(f'A soma de {n1} + {n2} é igual a {s}')
=======
numero1 = int(input('Digite \033[33mum número:\033[m '))
numero2 = int(input('Digite \033[33moutro número:\033[m '))
print(f'A soma de \033[33m{numero1} \033[31m+\033[m \033[33m{numero2}\033[m é igual a \033[33m{numero1+numero2}\033[m')
>>>>>>> Stashed changes
