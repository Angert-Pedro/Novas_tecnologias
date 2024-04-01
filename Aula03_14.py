#Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde
#você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
#posição está livre. Verifique também quando um jogador venceu a partida.
#Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual
#cada elemento é outra lista também com três elementos.
#for i in (grid)
   #if grid[i][0]==grid
"""grid = [[0,1,2], [0,1,2]]

print(grid[1][2])"""

grid = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def imprimir_grid():
    for linha in grid:
        for coluna in linha:
            print(coluna, end=' ')
        print()

def verificar_vitoria(simbolo):
    # Verificar linhas e colunas
    for i in range(3):
        if (grid[i][0] == grid[i][1] == grid[i][2] == simbolo) or \
           (grid[0][i] == grid[1][i] == grid[2][i] == simbolo):
            return True
    # Verificar diagonais
    if (grid[0][0] == grid[1][1] == grid[2][2] == simbolo) or \
       (grid[0][2] == grid[1][1] == grid[2][0] == simbolo):
        return True
    return False

def verificar_empate():
    for linha in grid:
        for coluna in linha:
            if coluna == ' ':
                return False
    return True

jogador = 'X'
acabou = False

while not acabou:
    imprimir_grid()
    print("Jogador", jogador)
    linha = int(input("Qual linha? "))
    coluna = int(input("Qual coluna? "))

    if grid[linha][coluna] != ' ':
        print("Posição já ocupada. Tente novamente.")
        continue

    grid[linha][coluna] = jogador

    if verificar_vitoria(jogador):
        acabou = True
        imprimir_grid()
        print("Jogador", jogador, "venceu!")
    elif verificar_empate():
        acabou = True
        imprimir_grid()
        print("Empate!")
    else:
        jogador = 'O' if jogador == 'X' else 'X'
