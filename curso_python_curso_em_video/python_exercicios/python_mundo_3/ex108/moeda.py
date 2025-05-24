def t():
    print('-' * 30)
def resumo (p, aumenta, diminui):
    t()
    print('RESUMO DO VALOR'.center(30))
    t()
    print(f'Preço analisado:'.ljust(20), moeda(p))
    print(f'Dobro do preço: '.ljust(20), dobro(p))
    print(f'Metade do preço: '.ljust(20), metade(p))
    print(f'{aumenta}% de aumento:'.ljust(20), aumentar(p, aumenta))
    print(f'{diminui}% de redução: '.ljust(20), diminuir(p, diminui))
    t()


def moeda(v = 0, format = True):
    res = f'R${v:.2f}'.replace('.',',')
    return res if format else v

def aumentar(v = 0, porcentagem=10):
    result = v + (porcentagem/100 * v)
    return moeda(result)


def diminuir(v = 0, porcentagem=10):
    result = v - (porcentagem/100 * v)
    return moeda(result)


def dobro(v = 0):
    result = v*2
    return moeda(result)


def metade(v = 0):
    result = v/2
    return moeda(result)