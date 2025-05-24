# 88) Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem várias vezes.
# Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
# +-------=======-------+
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# +-------=======-------+

def gerador(texto, quantidade):
    print('+-------=======-------+')
    for c in range(quantidade):
        print(texto)
    print('+-------=======-------+')

gerador("Aprendendo Portugol", 4)