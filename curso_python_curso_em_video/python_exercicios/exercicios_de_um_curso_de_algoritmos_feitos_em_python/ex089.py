# 89) Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que o programador possa escolher uma entre três bordas:
# +-------=======------+ Borda 1
# ~~~~~~~~:::::::~~~~~~~~ Borda 2
# <<<<<<<<------->>>>>>>> Borda 3
# Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
# ~~~~~~~~:::::::~~~~~~~~
# Portugol Studio
# Portugol Studio
# Portugol Studio
# ~~~~~~~~:::::::~~~~~~~~

def gerador(texto, quantidade, borda):
    bordas = ["+-------=======------+", "~~~~~~~~:::::::~~~~~~~~", "<<<<<<<<------->>>>>>>>"]
    print(bordas[borda-1])
    for c in range(quantidade):
        print(texto)
    print(bordas[borda-1])

gerador("Portugol Studio", 3, 2)