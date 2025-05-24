# 97) Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma adaptação que vai
# receber TRÊS números como parâmetro e vai retornar qual foi o maior entre eles.

def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    else:
        return "ERRO"
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

if maior(num1, num2, num3) == "ERRO":
    print("[Erro]: Informe 3 números diferentes!!!")
else:
    print(f'Entre os números {num1}, {num2} e {num3} o maior é {maior(num1, num2, num3)}')