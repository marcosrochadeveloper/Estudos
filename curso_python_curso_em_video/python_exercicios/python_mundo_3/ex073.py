# Ex073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Bahia.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
times = ('Internacional', 'Corinthians', 'Ceará SC', 'Fortaleza', 'Botafogo',
         'Flamengo', 'Palmeiras', 'Juventude', 'Fluminense', 'Grêmio',
         'Vasco da Gama', 'Cruzeiro', 'Bahia', 'São Paulo', 'Bragantino',
         'Santos', 'Mirassol', 'Sport Recife', 'Atlético-MG', 'EC Vitoria')

print(f'''a) Os 5 primeiros times da tabela são: {", ".join(times[:5])}
b) Os últimos 4 colocados da lista foram: {", ".join(times[-4:])}
c) Os times em ordem alfabética são: {", ".join(sorted(times))}
d) O time da Bahia, está na posição {times.index('Bahia')+1}''')