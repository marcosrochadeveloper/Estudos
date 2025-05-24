# 96) Crie um programa que tenha uma função Media(), que vai receber
# as 2 notas de um aluno e retornar a sua média para o programa principal.

def media(n1, n2):
    return (n1+n2)/2

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

print(f'A média do aluno foi {media(nota1, nota2):.1f}')
