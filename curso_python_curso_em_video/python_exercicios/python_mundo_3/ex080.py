# Ex080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
valores = []
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if len(valores) == 0 or valor >= valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for e, v in enumerate(valores):
            if valor <= v:
                valores.insert(e, valor)
                print(f'Adicionado na posição {e} da lista...')
                break
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')