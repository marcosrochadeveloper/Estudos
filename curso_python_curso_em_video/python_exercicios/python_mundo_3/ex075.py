# Ex075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#

valores = (int(input('Valor 1: ')), int(input('Valor 2: ')), int(input('Valor 3: ')), int(input('Valor 4: ')))
print(f'''A) O valor 9 apareceu {valores.count(9)} vezes
B) O número 3 {f'foi digitado primeiramente na posição {valores.index(3)}' if 3 in valores else 'NÃO FOI DIGITADO EM NENHUMA POSIÇÃO'}
C) Os números pares da tupla foram: ''', end ='')
for i in valores:
    if i%2 == 0:
        print(i, end= ' ')