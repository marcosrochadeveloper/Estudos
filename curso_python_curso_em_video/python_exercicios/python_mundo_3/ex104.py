# Ex104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
def leiaInt(n):
    print('-' * 30)
    while True:
        num = str(input(n))
        if num.isnumeric():
            num = int(num)
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m ')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')