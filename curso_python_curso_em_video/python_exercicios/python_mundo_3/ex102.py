# Ex102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
def fatorial(num, show = True):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = num
    print('-'*30)
    if show:
        print(num, end=' ')
    for num in range(num-1, 0, -1):
        if show:
            if num == 1:
                print('x', num, end=' = ')
            else:
                print('x',num, end= ' ')
        fat *= num
    return fat

print(fatorial(5))