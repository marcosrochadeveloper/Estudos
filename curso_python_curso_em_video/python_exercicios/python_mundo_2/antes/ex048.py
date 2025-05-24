# Ex048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# A soma de todos os 83 valores solicitados é 20667

ímpares = 0
total = 0
for c in range(0,500):
    if c%3 == 0 and c%2 == 1:
        ímpares = ímpares + c
        total = total + 1
print(f'A soma de todos os {total} valores solicitados é {ímpares}')