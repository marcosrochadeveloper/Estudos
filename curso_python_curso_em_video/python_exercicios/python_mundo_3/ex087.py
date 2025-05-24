# Ex087 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
matriz = [[0,0,0],[0,0,0],[0,0,0]]
tot_pares = tot_coluna3 = maior_segunda = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            tot_pares += matriz[l][c]
        if c == 2:
            tot_coluna3 += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior_segunda:
                maior_segunda = matriz[l][c]
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'''A) A soma de todos os valores pares digitados é {tot_pares}
B) A soma dos valores da terceira coluna é {tot_coluna3}
C) O maior valor da segunda linha é {maior_segunda}''')