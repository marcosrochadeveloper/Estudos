# Ex024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Em que cidade você nasceu? Rio de Janeiro
# False
# ---------------------------------------------
# Em que cidade você nasceu? Santo Antônio
# True

<<<<<<< Updated upstream
cidade = str(input('Em que cidade você nasceu? ').upper())
=======
cidade = str(input('Em que cidade você nasceu? ')).strip()
>>>>>>> Stashed changes
cidade = cidade.split()
print('SANTO' in cidade[0])
#print(cidade[0] == 'SANTO')