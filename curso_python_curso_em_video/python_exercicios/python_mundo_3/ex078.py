# Ex078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-'*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for e, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{e:.<4}', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for e, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{e:.<4}', end=' ')