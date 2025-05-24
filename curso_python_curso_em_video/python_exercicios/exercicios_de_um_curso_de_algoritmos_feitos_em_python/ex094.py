# 94) [DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado Fibonacci() que recebe um único valor inteiro
# como parâmetro, indicando quantos termos da sequência serão mostrados na tela.
# O seu procedimento deve receber esse valor e mostrar a quantidade de elementos solicitados.
# Obs: Use os exercícios 70 e 75 para te ajudar na solução
# Ex:
# Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
# Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> FIM


def fibonacci(quantidade):
    anterior = 0
    atual = 1
    proximo = 1
    for c in range(quantidade):
        print(atual, end=' >> ')
        anterior = atual
        atual = proximo
        proximo = anterior + atual
    print('FIM')

termos = int(input('Quantos termos da sequência de fibonacci quer que sejam exibidos? '))

fibonacci(termos)