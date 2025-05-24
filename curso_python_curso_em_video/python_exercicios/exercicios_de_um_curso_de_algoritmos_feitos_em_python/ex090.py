# 90) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento
# Somador() que vai calcular e mostrar a soma entre eles.

def somador(valor1, valor2):
    print(f'A soma entre {valor1} e {valor2} é igual a {valor1+valor2}')
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))

somador(num1, num2)