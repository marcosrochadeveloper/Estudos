# Ex026 - Faça um programa que leia uma frase pelo teclado e mostre:
# a) Quantas vezes aparece a letra “A”.
# b) Em que posição ela aparece a primeira vez.
# c) Em que posição ela aparece a última vez.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite uma frase: Amanda ama Pedro
<<<<<<< Updated upstream
# a) A letra A aparece 5 vezes na frase.
# b) A primeira letra A apareceu na posição 1
# c) A última letra A apareceu na posição 10

frase = str(input('Digite uma frase: ').strip().lower())
a = frase.count('a')
a1 = frase.find('a')
afinal = frase.rfind('a')
print(f'''a) A letra A aparece {a} vezes na frase.
b) A primeira letra A apareceu na posição {a1+1}
c) A última letra A apareceu na posição {afinal+1}''')
=======
# A letra A aparece 5 vezes na frase.
# A primeira letra A apareceu na posição 1
# A última letra A apareceu na posição 10

frase = str(input('Digite uma frase: ')).strip()
print(f'A \033[33mletra A\033[m aparece \033[33m{frase.lower().count('a')} vezes\033[m na frase.')
print(f'A \033[33mprimeira letra A\033[m apareceu na posição \033[33m{frase.lower().find('a')+1}\033[m')
print(f'A \033[33múltima letra A\033[m apareceu na posição \033[33m{frase.lower().rfind('a')+1}\033[m')
>>>>>>> Stashed changes
