#45) O programa anterior vai ter um problema quando digitarmos o primeiro valor
#maior que o último. Resolva esse problema com um código que funcione em qualquer situação.

primeiro_valor = int(input('Digite o primeiro Valor: '))
ultimo_valor = int(input('Digite o último Valor: '))
incremento = int(input('Digite o incremento: '))
c = primeiro_valor
print('Contagem: ', end='')
if primeiro_valor < ultimo_valor:
    while c < ultimo_valor:
        print(c, end=' ')
        c += incremento
    print('Acabou!')
elif primeiro_valor > ultimo_valor:
    if incremento > 0:
        incremento = -incremento
    while c > ultimo_valor:
        print(c, end=' ')
        c += incremento
    print('Acabou!')
else:
    print('[ERRO]: Primeiro e último valor iguais!')