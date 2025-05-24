'''lanche = ['Hamburger', 'Suco', 'Pizza', 'Picolé', 'Hamburger', 'Hamburger', 'Hamburger', 'Hamburger',]
lanche.append('Cookie')
lanche.insert(0,'Cachorro Quente')
del lanche[3] #Remove o item na posição 3 (Que seria a Pizza)
lanche.pop(3) #Remove o item na posição 3 (Que agora seria então o Picolé, porque a pizza já foi removida)
lanche.pop() #Remove o último item da lista
for c in range(len(lanche)):
    if 'Hamburger' in lanche:
        lanche.remove('Hamburger') #Remove o primeiro item que tenha escrito 'Hamburger'.
print(lanche)
valores = list(range(4, 11))
valores2 = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
valores2.sort(reverse=True) #Executa o comando sort() de forma reversa, do final para o começo
print(valores)
print(valores2)'''
número = [2, 5, 9, 1]

número[2] = 3
# [2, 5, 3, 1]

número.append(7)
# [2, 5, 3, 1, 7]

número.sort(reverse=True)
# [7, 5, 3, 2, 1]

número.insert(2, 2)
# [7, 5, 0, 3, 2, 1]

número.remove(2)

if 4 in número:
    número.remove(4)
else:
    print('Não achei o número 4')
print(número)
print(f'Essa lista em {len(número)} elementos.')