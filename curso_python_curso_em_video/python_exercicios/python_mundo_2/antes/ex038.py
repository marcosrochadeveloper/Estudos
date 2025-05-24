# Ex038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - o segundo valor é maior
# - Não existe valor maior, os dois são iguais
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro número: 4
# Segundo número: 1
# O PRIMEIRO valor é maior
#
# ---------------------------
#
# Primeiro número: 9
# Segundo número: 15
# O SEGUNDO valor é maior
#
# ----------------------------
#
# Primeiro número: 12
# Segundo número: 12
# Os dois valores são IGUAIS


numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

if numero1 > numero2:
    print('O \033[33mPRIMEIRO\033[m valor é maior')
elif numero2 > numero1:
    print('O \033[33mSEGUNDO\033[m valor é maior')
else:
    print('Os dois valores são \033[33mIGUAIS\033[m')