# 99) Faça um programa que possua uma função chamada Potencia(), que vai receber dois parâmetros numéricos
# (base e expoente) e vai calcular o resultado da exponenciação.
# Ex: Potencia(5,2) vai calcular 52 = 25

def potencia(base, expoente):
    return base**expoente

b = int(input('Informe o valor da base: '))
e = int(input('Informe o valor do expoente: '))

print(f'Calculando a potencia de {b} elevado a {e} chegamos no total de {potencia(b, e)}')