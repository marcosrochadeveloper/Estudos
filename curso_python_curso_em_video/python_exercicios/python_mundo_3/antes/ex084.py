pessoas = []
dados = []
total = 0
maispesados = [['',0]]
menospesados = [['',0]]
nomesmenospesados = []
nomesmaispesados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if menospesados[0][1] == 0:
        menospesados.clear()
        menospesados.append(dados[:])
        nomesmenospesados.append(dados[0])
    if dados[1] < menospesados[0][1]:
        menospesados.clear()
        nomesmenospesados.clear()
        nomesmenospesados.append(dados[0])
        menospesados.append(dados[:])
    elif dados[1] == menospesados[0][1]:
        menospesados.append(dados[:])
        nomesmenospesados.append(dados[0])
    if dados[1] > maispesados[0][1]:
        maispesados.clear()
        nomesmaispesados.clear()
        maispesados.append(dados[:])
        nomesmaispesados.append(dados[0])
    elif dados[1] == maispesados[0][1]:
        maispesados.append(dados[:])
        nomesmaispesados.append(dados[0])
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {total} pessoas.')
print(f'O maior peso foi {maispesados[0][1]}Kg. Peso de {nomesmaispesados}')
print(f'O menor peso foi {menospesados[0][1]}Kg. Peso de {nomesmenospesados}')