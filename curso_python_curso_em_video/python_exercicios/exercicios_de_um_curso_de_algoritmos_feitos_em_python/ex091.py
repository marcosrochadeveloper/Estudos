# 91) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um
# procedimento Maior() que vai verificar qual deles é o maior e mostrá-lo na tela.
# Caso os dois valores sejam iguais, mostrar uma mensagem informando essa característica.

def maior(valor1, valor2):
    if valor1 > valor2:
        print('O primeiro valor é maior')
    elif valor2 > valor1:
        print('O segundo valor é maior')
    else:
        print('Os valores são iguais!')
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
maior(num1, num2)
