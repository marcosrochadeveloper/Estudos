# 100) Melhore o exercício 96, criando além da função Media() uma outra função chamada Situacao(),
# que vai retornar para o programa principal se o aluno está APROVADO, em RECUPERAÇÃO ou REPROVADO.
# Essa nova função, vai receber como parâmetro o resultado retornado pela função Media().

def media(n1, n2):
    return (n1+n2)/2

def situacao():
    if media(nota1, nota2) < 4:
        return "\033[31mREPROVADO\033[m"
    elif media(nota1, nota2) < 7:
        return "\033[33mEM RECUPERAÇÃO\033[m"
    else:
        return "\033[32mAPROVADO\033[m"

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

print(f'A média do aluno foi {media(nota1, nota2):.1f} e ele está {situacao()}')