def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip()
        if valor.count(',') > 0:
            valor = valor.replace(',','.')
        if not valor.isdigit():
            if valor.count('.') == 1:
                valor = float(valor)
                break
            else:
                print(f'\033[31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            valor = float(valor)
            break
    return valor