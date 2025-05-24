# 92) Crie uma lógica que leia um número inteiro e passe para um procedimento ParOuImpar()
# que vai verificar e mostrar na tela se o valor passado como parâmetro é PAR ou ÍMPAR.

def par_ou_impar(v1):
    if v1%2 == 0:
        print('O valor informado é Par')
    else:
        print('O valor informado é Ímpar')

valor = int(input('Informe um valor: '))

par_ou_impar(valor)