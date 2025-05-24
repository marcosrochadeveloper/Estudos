# Ex053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite uma frase: apos a sopa
# O inverso de APOSASOPA é APOSASOPA
# Temos um palíndromo!

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper().split()
frase = ''.join(frase)
inverso = []
for c in range (len(frase)-1,-1,-1):
    inverso.append(frase[c])
inverso = ''.join(inverso)
print(f'O inverso de {frase} é {inverso}')
print('Temos um palíndromo!') if frase == inverso else print('A frase digitada não é um palíndromo!')