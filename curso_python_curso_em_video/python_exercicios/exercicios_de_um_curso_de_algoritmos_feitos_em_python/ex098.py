# 98) Crie um programa que tenha uma função SuperSomador(), que vai receber dois números como parâmetro e depois
# vai retornar a soma de todos os valores no intervalo entre os valores recebidos.
# Ex:
# SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
# SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85

def super_somador(n1, n2):
    c = n1
    soma = 0
    while c <= n2:
        soma += c
        c += 1
    return soma

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(f'A soma de todos os números entre {num1} e {num2} incluindo eles mesmos é igual a {super_somador(num1, num2)}')