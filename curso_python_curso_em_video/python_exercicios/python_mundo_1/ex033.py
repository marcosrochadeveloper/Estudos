# Ex033 - Faça um programa que leia 3 números, e mostre qual é o maior e qual é o menor.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro valor: 7
# Segundo valor: 2
# Terceiro valor: 4
# O menor valor digitado foi 2
# O maior valor digitado foi 7
<<<<<<< Updated upstream
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
maior = num1
menor = num1
if num2 > maior and num2 > num3:
    maior = num2
if num3 > maior and num3 > num2:
    maior = num3
if num2 < menor and num2 < num3:
    menor = num2
if num3 < menor and num3 < num2:
    menor = num3
print(f'''O menor valor digitado foi {menor}
O maior valor digitado foi {maior}''')
=======

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))
maior = valor1 if valor1 > valor2 and valor3 else valor2
maior = valor3 if valor3 > maior else maior
menor = valor1 if valor1 < valor2 and valor3 else valor2
menor = valor3 if valor3 < menor else menor
print(f'O menor valor digitado foi \033[31m{menor}\033[m')
print(f'O maior valor digitado foi \033[32m{maior}\033[m')
>>>>>>> Stashed changes
