# Ex037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número inteiro: 234
# Escolha uma das bases para conversão:
# [ 1 ] Converter para BINÁRIO
# [ 2 ] Converter para OCTAL
# [ 3 ] Converter para HEXADECIMAL
# Sua opção: 3
# 234 convertido para HEXADECIMAL é igual a ea
#
# ------------------------------------
# Sua opção: 1
# 234 convertido para BINÁRIO é igual a 11101010
# -------------------------------------
#
# Sua opção: 2
# 234 convertido para OCTAL é igual a 352

número = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    #print(f'{número} convertido para BINÁRIO é igual a {número:b}')
    print(f'{número} convertido para BINÁRIO é igual a {bin(número)[2:]}')
elif opção == 2:
    #print(f'{número} convertido para OCTAL é igual a {número:o}')
    print(f'{número} convertido para OCTAL é igual a {oct(número)[2:]}')
elif opção == 3:
    #print(f'{número} convertido para HEXADECIMAL é igual a {número:x}')
    print(f'{número} convertido para HEXADECIMAL é igual a {hex(número)[2:]}')
else:
    print('OPÇÃO INVÁLIDA! Tente novamente!')
