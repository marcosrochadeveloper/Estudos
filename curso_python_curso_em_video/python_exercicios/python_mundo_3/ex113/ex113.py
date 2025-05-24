# Ex113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
def leiaInt(n):
    while True:
        try:
            num = int(input(n).strip())
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido.\033[m ')
        except KeyboardInterrupt:
            print('\033[31m\nEntrada de dados interrompida pelo usuário.\033[m ')
            return 0
        else:
            return num


def leiaFloat(n):
    while True:
        try:
            num = str(input(n)).strip()
            if num.count(',') == 1:
                num = num.replace(',', '.')
                num = float(num)
            elif num != '':
                num = float(num)
            else:
                print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
                num = 0
                return num
        except:
            print(f'\033[31mERRO: por favor digite um número válido.\033[m')
        else:
            return num

inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')