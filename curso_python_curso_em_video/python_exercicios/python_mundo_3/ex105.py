# Ex105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :parameter n: uma ou mais notas dos alunos (aceita várias)
    :parameter sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    info = dict()
    info['Total'] = len(n)
    info['Maior'] = max(n)
    info['Menor'] = min(n)
    info['Média'] = f'{sum(n) / len(n):.2f}'
    if sit:
        if info['Média'] < 5:
            situacao = 'RUIM'
        elif info['Média'] < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        info['Situação'] = situacao
    return info

resp = notas(5.5, 2.5, 6.5, 7.5, sit=True)
print(resp)
