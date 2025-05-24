tabuleiro = [[1,2,3], [4,5,6], [7,8,9]]
c = 1
while True:
    print(f'''
    +---+---+---+
    | {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |
    +---+---+---+
    | {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |
    +---+---+---+
    | {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |
    +---+---+---+
    ''')

    if c % 2 != 0:
        jogada = int(input('Vai jogar [X] em qual posição? '))
        jg = 'X'
    else:
        jogada = int(input('Vai jogar [O] em qual posição? '))
        jg = 'O'

    if jogada == 1:
        tabuleiro[0][0] = jg
    elif jogada == 2:
        tabuleiro[0][1] = jg
    elif jogada == 3:
        tabuleiro[0][2] = jg
    elif jogada == 4:
        tabuleiro[1][0] = jg
    elif jogada == 5:
        tabuleiro[1][1] = jg
    elif jogada == 6:
        tabuleiro[1][2] = jg
    elif jogada == 7:
        tabuleiro[2][0] = jg
    elif jogada == 8:
        tabuleiro[2][1] = jg
    elif jogada == 9:
        tabuleiro[2][2] = jg
    c += 1
    if c > 10:
        break
