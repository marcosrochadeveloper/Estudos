palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('a','e','i','o','u')
for palavra in palavras:
    atual = palavra
    print(f'Na palavra {palavra} temos ', end='')
    for c in range(len(atual)):
        if atual[c].lower() in vogais:
            print(atual[c].lower(),end=' ')
    print('')