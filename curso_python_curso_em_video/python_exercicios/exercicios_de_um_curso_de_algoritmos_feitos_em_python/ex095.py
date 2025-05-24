# 95) Refaça o exercício 90, só que agora em forma de função Somador(), que vai receber dois parâmetros
# e vai retornar o resultado da soma entre eles para o programa principal.

def somador(v1, v2):
    return v1+v2

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

print(f'A soma entre {valor1} e {valor2} é igual a {somador(valor1, valor2)}')
