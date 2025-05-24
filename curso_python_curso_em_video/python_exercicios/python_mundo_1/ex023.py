# Ex023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
<<<<<<< Updated upstream
# Informe um número entre 0 e 9999: 9876
=======
# Informe um número: 9876
>>>>>>> Stashed changes
# Analisando o número 9876
# Unidade: 6
# Dezena: 7
# Centena: 8
# Milhar: 9

<<<<<<< Updated upstream
num = int(input('Informe um número entre 0 e 9999: '))
print(f'Analisando o número {num}')
print(f'''Unidade: {num%10}
Dezena: {(num%100)//10}
Centena: {(num%1000)//100}
Milhar: {(num%10000)//1000}
''')
=======
número = int(input('Informe um número: '))
print(f'Analisando o número \033[33m{número}\033[m')
print(f'Unidade: \033[33m{número % 10}\033[m')
print(f'Dezena: \033[33m{número // 10 % 10}\033[m')
print(f'Centena: \033[33m{número // 100 % 10}\033[m')
print(f'Milhar: \033[33m{número // 1000 % 10}\033[m')
>>>>>>> Stashed changes
