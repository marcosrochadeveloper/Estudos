# Ex083 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
expressao = str(input('Informe a expressão: '))
parenteses = []
for i in expressao:
    if i == '(':
        parenteses.append(i)
    if i == ')':
        if not parenteses:
            parenteses.append(i)
            break
        else:
            parenteses.pop()
if not parenteses:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
