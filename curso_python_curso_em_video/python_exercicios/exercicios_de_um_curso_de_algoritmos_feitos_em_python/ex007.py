#7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
#Ex:
#Digite um número: 3.5
#O dobro de 3.5 é 7.0
#A terça parte de 3.5 é 1.16666

número = float(input('Digite um número: '))
print(f'O dobro de {número} é {número*2}')
print(f'A terça parte de {número} é {número / 3:.2f}')