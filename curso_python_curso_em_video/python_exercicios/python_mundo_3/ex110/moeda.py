def t():
    print('-' * 30)


def resumo (v = 0, aumenta = 10, diminui = 5):
    if v.count(',') == 1:
        v = float(v.replace(',', '.'))
    else:
        v = float(v)
    t()
    print('RESUMO DO VALOR'.center(30))
    t()
    print(f'Preço analisado:'.ljust(20), moeda(str(v)))
    print(f'Dobro do preço: '.ljust(20), dobro(v))
    print(f'Metade do preço: '.ljust(20), metade(v))
    print(f'{aumenta}% de aumento:'.ljust(20), aumentar(v, aumenta))
    print(f'{diminui}% de redução: '.ljust(20), diminuir(v, diminui))
    t()


def moeda(v = 0, format = True):
    res = v
    if type(res) == str:
        if res.count(',') == 1:
            res = float(res.replace(',', '.'))
        else:
            res = float(res)
    res = f'R${res:.2f}'.replace('.',',')
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