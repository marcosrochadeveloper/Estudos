#6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
#Ex:
#Digite um número: 9
#O antecessor de 9 é 8
#O sucessor de 9 é 10

número = int(input('Digite um número: '))
print(f'O antecessor de {número} é {número-1}')
print(f'O sucessor de {número} é {número+1}')