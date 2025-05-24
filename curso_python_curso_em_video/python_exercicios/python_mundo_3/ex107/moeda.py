def aumentar(v, porcentagem=10):
    result = v + (porcentagem/100 * v)
    return result


def diminuir(v, porcentagem=10):
    result = v - (porcentagem/100 * v)
    return result


def dobro(v):
    result = v*2
    return result


def metade(v):
    result = v/2
    return result