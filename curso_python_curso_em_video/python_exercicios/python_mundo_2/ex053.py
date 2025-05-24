# Ex053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite uma frase: apos a sopa
# O inverso de APOSASOPA é APOSASOPA
# Temos um palíndromo!

frase = str(input('Digite uma frase: ').strip().upper())
palavras = frase.split()
junto = "".join(palavras)
'''frase_inversa = ''
for c in range(len(junto)-1,-1,-1):
    frase_inversa += junto[c]'''
frase_inversa = junto[::-1]
print(f'O inverso de {junto} é {frase_inversa}')
if junto == frase_inversa:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
