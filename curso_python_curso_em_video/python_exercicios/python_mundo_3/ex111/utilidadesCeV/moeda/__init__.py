def t():
    print('-' * 30)
def resumo (p = 0, aumenta = 10, diminui = 5):
    if p.count(',') == 1:
        p = float(p.replace(',', '.'))
    else:
        p = float(p)
    t()
    print('RESUMO DO VALOR'.center(30))
    t()
    print(f'Preço analisado:'.ljust(20), moeda(p))
    print(f'Dobro do preço: '.ljust(20), dobro(p))
    print(f'Metade do preço: '.ljust(20), metade(p))
    print(f'{aumenta}% de aumento:'.ljust(20), aumentar(p, aumenta))
    print(f'{diminui}% de redução: '.ljust(20), diminuir(p, diminui))
    t()


def moeda(v, format = True):
    res = v
    if type(res) == str:
        if res.count(',') == 1:
            res = float(res.replace(',', '.'))
        else:
            res = float(res)
    res = f'R${res:.2f}'.replace('.',',')
    return res if format else v

def aumentar(v, porcentagem=10):
    result = v + (porcentagem/100 * v)
    return moeda(result)


def diminuir(v, porcentagem=10):
    result = v - (porcentagem/100 * v)
    return moeda(result)


def dobro(v):
    result = v*2
    return moeda(result)


def metade(v):
    result = v/2
    return moeda(result)