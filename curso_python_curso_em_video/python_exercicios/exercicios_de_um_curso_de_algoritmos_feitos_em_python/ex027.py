#27) Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média até 4.9: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
try:
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        media = (nota1+nota2)/2

        if media <= 4.9:
            print('Aluno \033[31mREPROVADO\033[m!')
        elif media <= 6.9:
            print('Aluno em \033[33mRECUPERAÇÃO\033[m!')
        else:
            print('Aluno \033[32mAPROVADO\033[m!')

    else:
        print('As notas devem estar entre 0 e 10.')

except ValueError:
    print('Entrada inválida! Informe um número Real Válido!')