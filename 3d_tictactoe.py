# Feito por:
## Made by:

# Guilherme de Menezes Furtado
# Guilherme da Silva Gadelha

import os
import random

# Função que limpa o prompt.
## Clears the prompt.
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicia o game.
## Starts the game.
def game(tab, scoreBot, scorePlayer):
    
    player(tab, simbolo(), scoreBot, scorePlayer)

# Printa as 3 camadas em seu estado atual.
## Prints the 3 z layers of the matriz in its present state.
def printTabuleiro(tab): 
    print("  CAMADA  1     CAMADA  2     CAMADA  3")
    print("  1   2   3     1   2   3     1   2   3")
    print("1 " + tab[0][0][0] + " | " + tab[0][0][1] + " | " + tab[0][0][2] + "   1 " + tab[1][0][0] + " | " + tab[1][0][1] + " | " + tab[1][0][2] + "   1 " + tab[2][0][0] + " | " + tab[2][0][1] + " | " + tab[2][0][2])
    print(" ---+---+---   ---+---+---   ---+---+---")
    print("2 " + tab[0][1][0] + " | " + tab[0][1][1] + " | " + tab[0][1][2] + "   2 " + tab[1][1][0] + " | " + tab[1][1][1] + " | " + tab[1][1][2] + "   2 " + tab[2][1][0] + " | " + tab[2][1][1] + " | " + tab[2][1][2])
    print(" ---+---+---   ---+---+---   ---+---+---")
    print("3 " + tab[0][2][0] + " | " + tab[0][2][1] + " | " + tab[0][2][2] + "   3 " + tab[1][2][0] + " | " + tab[1][2][1] + " | " + tab[1][2][2] + "   3 " + tab[2][2][0] + " | " + tab[2][2][1] + " | " + tab[2][2][2])

# Recebe o símbolo que o jogador quer usar.
## Receives the symbol that the player will use.
def simbolo():

    cls()

    inp = input("Escolha o seu símbolo:\n\nX\nO\n\n")

    if inp == "X" or inp == "x":

        simb = "X"
        cls()
        return simb

    elif inp == "O" or inp == "o":

        simb = "O"
        cls()
        return simb

    else:
        cls()
        print("Por favor, escolha um símbolo válido!")
        simb = simbolo()
        return simb

# Recebe o símbolo usado pelo jogador e seleciona o outro para o bot/máquina e executa os algoritmos de jogada.
## Receives the symbol used by the player and selects the other for the bot. Then executes the play algorithms.
def bot(tab, l, scoreBot, scorePlayer):

    print("\nAgora é a vez do seu adversário:\n")

    if l == "X":
        simbot = "O"
    else:
        simbot = "X"

    jogando = True

    jogadasBot = [jogadaVencedora1, jogadaVencedora2, bloqVit1, bloqVit2, criarSequ1, criarSequ2, jogarEmVazio1, jogarEmVazio2, jogarQualquer]

    i = 0

    while jogando == True and i < len(jogadasBot):
        jogando = jogadasBot[i](tab, simbot, l, scoreBot, scorePlayer)
        i += 1

# Recebe as coordenadas do jogador e aplica o símbolo à posição no tabuleiro.
## Receives the input coordinates from the player and aplies the symbol to that space.
def player(tab, k, scoreBot, scorePlayer):

    printTabuleiro(tab)

    simb = k
    cont = 0
    num = False
    x = 0
    y = 0
    z = 0

    coord = input("\nInsira as coordenadas da sua próxima jogada, na seguinte ordem: camada, linha, coluna \n\n")
    
    cls()
    coord = list(coord)

    
    for i in coord:
        if i == '1' or i == '2' or i == '3':

            num = True
            cont += 1
        else:
            num = False

        if cont == 1 and num:
            z = int(i) - 1

        elif cont == 2 and num:
            x = int(i) - 1

        elif cont == 3 and num:
            y = int(i) - 1
    
    if cont != 3:

        cls()
        print("Por favor, insira coordenadas válidas!\n")
        player(tab, k, scoreBot, scorePlayer)

    elif tab[z][x][y] != " ":
        
        cls()
        print("Por favor, insira coordenadas válidas!\n")
        player(tab, k, scoreBot, scorePlayer)

    else:

        tab[z][x][y] = k
        verificarEmpate(tab, k, scoreBot, scorePlayer, False)

# Pergunta se o player gostaria de jogar de novo.
## Asks if the player would like to play again.
def deNovo(tab, scoreBot, scorePlayer):

    escolha = input("\nVocê gostaria de jogar de novo?\n\n1 = Sim!    :)\n2 = Não... :(\n\n")

    if escolha == "1":
        tab = [[[" " for i in range(0, 3)] for i in range(0, 3)]for i in range (0, 3)]
        game(tab, scoreBot, scorePlayer)
    elif escolha != "2":
        print("Escolha um número válido!")
        deNovo(tab, scoreBot, scorePlayer)

# Mostra o vencedor e o placar e pergunta se o player gostaria de jogar de novo.
## Shows the winner and the score, then asks if the player would like to play again.
def telaFinal(tab, vencedor, scoreBot, scorePlayer):
    printTabuleiro(tab)

    if vencedor == "Bot":
        scoreBot += 1
    elif vencedor == "Jogador":
        scorePlayer += 1
    else:
        vencedor = "Ninguém"
    
    print("\n" + vencedor + " venceu!")
    print("\nPlacar:\n\nJogador:", scorePlayer, "\nBot:", scoreBot)

    deNovo(tab, scoreBot, scorePlayer)



# Algoritmos de jogada do bot em ordem de prioridade decrescente:
## Bot play algorithms in descending priority order:



# Verifica por situações onde o bot vence e que não envolvem mais de uma camada z.
## Checks for situations where the bot wins and it doesn't involve more than one z layer.
def jogadaVencedora1(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    z = 0
    while z < 3 and jogando:

        x = 0
        while x < 3 and jogando:

            y = 0
            vazio = False
            cont = 0

            while y < 3 and jogando:

                if tab[z][x][y] == simbot:
                    cont += 1

                elif tab[z][x][y] == " ":
                    coordVazio = y
                    vazio = True

                else:
                    vazio = False
                
                if cont == 2 and vazio:
                    tab[z][x][coordVazio] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", z + 1, x + 1, coordVazio + 1, "\n")
                    telaFinal(tab, "Bot", scoreBot, scorePlayer)
                y += 1
            x += 1
        z += 1

    z = 0
    while z < 3 and jogando:
        
        y = 0
        while y < 3 and jogando:

            x = 0
            vazio = False
            cont = 0

            while x < 3 and jogando:

                if tab[z][x][y] == simbot:
                    cont += 1

                elif tab[z][x][y] == " ":
                    coordVazio = x
                    vazio = True

                else:
                    vazio = False
                
                if cont == 2 and vazio:
                    tab[z][coordVazio][y] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", z + 1, coordVazio + 1, y + 1, "\n")
                    telaFinal(tab, "Bot", scoreBot, scorePlayer)
                x += 1 
            y += 1
        z += 1

    z = 0
    while z < 3 and jogando:
        
        xy = 0
        vazio = False
        cont = 0

        while xy < 3 and jogando:
                    
            if tab[z][xy][xy] == simbot:
                cont += 1

            elif tab[z][xy][xy] == " ":
                coordVazio = xy
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[z][coordVazio][coordVazio] = simbot
                jogando = False
                    
                print("Ele escolheu as coordenadas", z + 1, coordVazio + 1, coordVazio + 1, "\n")
                telaFinal(tab, "Bot", scoreBot, scorePlayer)
            
            xy += 1
        z += 1 
    
    z = 0
    while z < 3 and jogando:
        
        dif = 0
        vazio = False
        cont = 0

        while dif < 3 and jogando:

            x = dif
            y = 2 - dif

            if tab[z][x][y] == simbot:
                cont += 1

            elif tab[z][x][y] == " ":
                coordVazioX = x
                coordVazioY = y
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[z][coordVazioX][coordVazioY] = simbot
                jogando = False
                    
                print("Ele escolheu as coordenadas", z + 1, coordVazioX + 1, coordVazioY + 1, "\n")
                telaFinal(tab, "Bot", scoreBot, scorePlayer)
            dif += 1
        z += 1
    return jogando

# A mesma coisa, mas envolvendo mais de uma camada z.
## The same thing, but involving more than one z layer.
def jogadaVencedora2(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    x = 0
    while x < 3 and jogando:
      
        y = 0

        while y < 3 and jogando:

            z = 0
            cont = 0
            vazio = False

            while z < 3 and jogando:

                if tab[z][x][y] == simbot:
                    cont += 1
            
                elif tab[z][x][y] == " ":
                    vazio = True
                    coordVazio = z
            
                else:
                    vazio = False
            
                if cont == 2 and vazio:
                    tab[coordVazio][x][y] = simbot
                    jogando = False

                    print("Ele escolheu as coordenadas", coordVazio + 1, x + 1, y + 1, "\n")
                    telaFinal(tab, "Bot", scoreBot, scorePlayer)
                
                z += 1
            y += 1
        x += 1

    x = 0
    while x < 3 and jogando:

        zy = 0
        cont = 0
        vazio = False

        while zy < 3 and jogando:
                    
            if tab[zy][x][zy] == simbot:
                cont += 1

            elif tab[zy][x][zy] == " ":
                coordVazio = zy
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[coordVazio][x][coordVazio] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazio + 1, x + 1, coordVazio + 1, "\n")
                telaFinal(tab, "Bot", scoreBot, scorePlayer)
              
            zy += 1
        x +=1
    
    x = 0
    while x < 3 and jogando:

        dif = 0
        cont = 0
        vazio = False

        while dif < 3 and jogando:
            
            z = dif
            y = 2 - dif
                    
            if tab[z][x][y] == simbot:
                cont += 1

            elif tab[z][x][y] == " ":
                coordVazioZ = z
                coordVazioY = y
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[coordVazioZ][x][coordVazioY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazioZ + 1, x + 1, coordVazioY + 1, "\n")
                telaFinal(tab, "Bot", scoreBot, scorePlayer)

            dif += 1
        x +=1

    y = 0
    while y < 3 and jogando:

        zx = 0
        cont = 0
        vazio = False

        while zx < 3 and jogando:
 
            if tab[zx][zx][y] == simbot:
                cont += 1

            elif tab[zx][zx][y] == " ":
                coordVazio = zx
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[coordVazio][coordVazio][y] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazio + 1, coordVazio + 1, y + 1, "\n")
                telaFinal(tab, "Bot", scoreBot, scorePlayer)
            
            zx += 1
        y += 1

    y = 0
    while y < 3 and jogando:

        dif = 0
        cont = 0
        vazio = False

        while dif < 3 and jogando:
            
            z = dif
            x = 2 - dif

            if jogando == False:
                break

            if jogando == False:
                break
                    
            if tab[z][x][y] == simbot:
                cont += 1

            elif tab[z][x][y] == " ":
                coordVazioZ = z
                coordVazioX = x
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[coordVazioZ][coordVazioX][y] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazioZ + 1, coordVazioX + 1, y + 1, "\n")
                telaFinal(tab, "Bot", scoreBot, scorePlayer)
            
            dif += 1
        y += 1

    # Verifica por possíveis jogadas ganhadoras nas diagonais espaciais do tabuleiro.
    ## Checks for winning plays in the matrix's 3D diagonals.

    cont = 0
    vazio = False
    

    ## 1
    xyz = 0
    while xyz < 3 and jogando:

        if tab[xyz][xyz][xyz] == simbot:
            cont += 1

        elif tab[xyz][xyz][xyz] == " ":
            coordVazio = xyz
            vazio = True

        else:
            vazio = False
                
        if cont == 2 and vazio:
            tab[coordVazio][coordVazio][coordVazio] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazio + 1, coordVazio + 1, coordVazio + 1, "\n")
            telaFinal(tab, "Bot", scoreBot, scorePlayer)

        xyz += 1
    
    cont = 0
    vazio = False
    
    
    ## 2
    dif = 0
    while dif < 3 and jogando:

        x = 2 - dif
        zy = dif

        if tab[zy][x][zy] == simbot:
            cont += 1

        elif tab[zy][x][zy] == " ":
            coordVazioZY = zy
            coordVazioX = x
            vazio = True

        else:
            vazio = False
                
        if cont == 2 and vazio:
            tab[coordVazioZY][coordVazioX][coordVazioZY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazioZY + 1, coordVazioX + 1, coordVazioZY + 1, "\n")
            telaFinal(tab, "Bot", scoreBot, scorePlayer)

        dif += 1

    cont = 0
    vazio = False

    ## 3
    dif = 0
    while dif < 3 and jogando:

        y = 2 - dif
        zx = dif

        if jogando == False:
            break
                    
        if tab[zx][zx][y] == simbot:
            cont += 1

        elif tab[zx][zx][y] == " ":
            coordVazioZX = zx
            coordVazioY = y
            vazio = True

        else:
            vazio = False
                
        if cont == 2 and vazio:
            tab[coordVazioZX][coordVazioZX][coordVazioY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazioZX + 1, coordVazioZX + 1, coordVazioY + 1, "\n")
            telaFinal(tab, "Bot", scoreBot, scorePlayer)

        dif += 1

    cont = 0
    vazio = False

    ## 4
    dif = 0
    while dif < 3 and jogando:

        z = dif
        xy = 2 - dif
 
        if tab[z][xy][xy] == simbot:
            cont += 1

        elif tab[z][xy][xy] == " ":
            coordVazioXY = xy
            coordVazioZ = z
            vazio = True

        else:
            vazio = False

        
        if cont == 2 and vazio:
            tab[coordVazioZ][coordVazioXY][coordVazioXY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazioZ + 1, coordVazioXY + 1, coordVazioXY + 1, "\n")
            telaFinal(tab, "Bot", scoreBot, scorePlayer)
        
        dif += 1
        
    return jogando

# Impede o jogador de completar uma sequência na próxima jogada.
## Stops the player from completing a full sequence in the next play. 
def bloqVit1(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    z = 0
    while z < 3 and jogando:

        x = 0
        while x < 3 and jogando:

            y = 0
            vazio = False
            cont = 0

            while y < 3 and jogando:

                if tab[z][x][y] == l:
                    cont += 1
          
                elif tab[z][x][y] == " ":

                    coordVazio = y
                    vazio = True
          
                elif tab[z][x][y] == simbot:
                    vazio = False

                if cont == 2 and vazio:

                    tab[z][x][coordVazio] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", z + 1, x + 1, coordVazio + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)

                y += 1
            x += 1
        z += 1
          
    z = 0
    while z < 3 and jogando:

        y = 0
        while y < 3 and jogando:

            x = 0
            vazio = False
            cont = 0

            while x < 3 and jogando:

                if tab[z][x][y] == l:
                    cont += 1

                elif tab[z][x][y] == " ":
                    coordVazio = x
                    vazio = True

                elif tab[z][x][y] == simbot:
                    vazio = False
                
                if cont == 2 and vazio:
                    tab[z][coordVazio][y] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", z + 1, coordVazio + 1, y + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)
              
                x += 1
            y += 1
        z += 1

    z = 0
    while z < 3 and jogando:

        xy = 0
        vazio = False
        cont = 0

        while xy < 3 and jogando:
                    
            if tab[z][xy][xy] == l:
                cont += 1

            elif tab[z][xy][xy] == " ":
                coordVazio = xy
                vazio = True

            elif tab[z][xy][xy] == simbot:
                vazio = False
                
            if cont == 2 and vazio:
                tab[z][coordVazio][coordVazio] = simbot
                jogando = False
                    
                print("Ele escolheu as coordenadas", z + 1, coordVazio + 1, coordVazio + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            xy += 1
        z += 1

    z = 0
    while z < 3 and jogando:

        dif = 0
        vazio = False
        cont = 0

        while dif < 3 and jogando:

            x = 0 + dif
            y = 2 - dif

            if jogando == False:
                break
                    
            if tab[z][x][y] == l:
                cont += 1

            elif tab[z][x][y] == " ":
                coordVazioX = x
                coordVazioY = y
                vazio = True

            elif tab[z][x][y] == simbot:
                vazio = False
                
            if cont == 2 and vazio:
                tab[z][coordVazioX][coordVazioY] = simbot
                jogando = False
                    
                print("Ele escolheu as coordenadas", z + 1, coordVazioX + 1, coordVazioY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)

            dif += 1
        z += 1

    return jogando

# A mesma coisa, mas envolvendo mais de uma camada z.
## The same thing, but involving more than one z layer.
def bloqVit2(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True 

    x = 0
    while x < 3 and jogando:

        y = 0
        while y < 3 and jogando:

            z = 0     
            cont = 0
            vazio = False

            while z < 3 and jogando:
                    
                if tab[z][x][y] == l:
                    cont += 1
            
                elif tab[z][x][y] == " ":
                    vazio = True
                    coordVazio = z
            
                else:
                    vazio = False
            
                if cont == 2 and vazio:
                    tab[coordVazio][x][y] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", coordVazio + 1, x + 1, y + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)
                
                z += 1
            y += 1
        x += 1
    
    x = 0
    while x < 3 and jogando:

        zy = 0
        cont = 0
        vazio = False

        while zy < 3 and jogando:
            
            if tab[zy][x][zy] == l:
                cont += 1

            elif tab[zy][x][zy] == " ":
                coordVazio = zy
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[coordVazio][x][coordVazio] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazio + 1, x + 1, coordVazio + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            zy += 1
        x += 1

    x = 0
    while x < 3 and jogando:

        dif = 0
        cont = 0
        vazio = False

        while dif < 3 and jogando:
            
            z = dif
            y = 2 - dif

            if tab[z][x][y] == l:
                cont += 1

            elif tab[z][x][y] == " ":
                coordVazioZ = z
                coordVazioY = y
                vazio = True

            else:
                vazio = False
                
            if cont == 2 and vazio:
                tab[coordVazioZ][x][coordVazioY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazioZ + 1, x + 1, coordVazioY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)

            dif += 1
        x += 1

    y = 0
    while y < 3 and jogando:

        zx = 0
        cont = 0
        vazio = False

        while zx < 3 and jogando:
                    
            if tab[zx][zx][y] == l:
                cont += 1

            elif tab[zx][zx][y] == " ":
                coordVazio = zx
                vazio = True
    
            if cont == 2 and vazio:
                tab[coordVazio][coordVazio][y] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazio + 1, coordVazio + 1, y + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)

            zx += 1
        y += 1
  
    y = 0
    while y < 3 and jogando:

        dif = 0
        cont = 0
        vazio = False

        while dif < 3 and jogando:
            
            z = dif
            x = 2 - dif
                    
            if tab[z][x][y] == l:
                cont += 1

            elif tab[z][x][y] == " ":
                coordVazioZ = z
                coordVazioX = x
                vazio = True

            else:
                vazio = False
            
            if cont == 2 and vazio:
                tab[coordVazioZ][coordVazioX][y] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", coordVazioZ + 1, coordVazioX + 1, y + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            dif += 1
        y += 1


    cont = 0
    vazio = False

    # 1
    xyz = 0
    while xyz < 3 and jogando:
                    
        if tab[xyz][xyz][xyz] == l:
            cont += 1

        elif tab[xyz][xyz][xyz] == " ":
            coordVazio = xyz
            vazio = True

        else:
            vazio = False
                
        if cont == 2 and vazio:
            tab[coordVazio][coordVazio][coordVazio] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazio + 1, coordVazio + 1, coordVazio + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        xyz += 1
    
    cont = 0
    vazio = False
    
    # 2
    dif = 0
    while dif < 3 and jogando:

        x = 2 - dif
        zy = dif
 
        if tab[zy][x][zy] == l:
            cont += 1

        elif tab[zy][x][zy] == " ":
            coordVazioZY = zy
            coordVazioX = x
            vazio = True

        else:
            vazio = False
                
        if cont == 2 and vazio:
            tab[coordVazioZY][coordVazioX][coordVazioZY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazioZY + 1, coordVazioX + 1, coordVazioZY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        dif += 1

    cont = 0
    vazio = False

    # 3
    dif = 0
    while dif < 3 and jogando:

        y = 2 - dif
        zx = dif
 
        if tab[zx][zx][y] == l:
            cont += 1

        elif tab[zx][zx][y] == " ":
            coordVazioZX = zx
            coordVazioY = y
            vazio = True

        else:
            vazio = False
                
        if cont == 2 and vazio:
            tab[coordVazioZX][coordVazioZX][coordVazioY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazioZX + 1, coordVazioZX + 1, coordVazioY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        dif += 1

    cont = 0
    vazio = False

    # 4
    dif = 0
    while dif < 3 and jogando:
        
        z = dif
        xy = 2 - dif
                    
        if tab[z][xy][xy] == l:
            cont += 1

        elif tab[z][xy][xy] == " ":
            coordVazioXY = xy
            coordVazioZ = z
            vazio = True

        else:
            vazio = False

        
        if cont == 2 and vazio:
            tab[coordVazioZ][coordVazioXY][coordVazioXY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", coordVazioZ + 1, coordVazioXY + 1, coordVazioXY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        dif += 1

    return jogando

# Verifica por situações onde se pode criar sequências de 2 símbolos + um espaço vazio que não envolvem mais de uma camada.
## Checks for situations where it can create 2 symble + 1 empty space sequences where it doesn't involve more than one z layer.
def criarSequ1(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    z = 0
    while z < 3 and jogando:

        x = 0
        while x < 3 and jogando:

            y = 0
            simbolo = False
            vazioCont = 0
            coordenadas = []

            while y < 3 and jogando:

                if tab[z][x][y] == " ":
                    vazioCont += 1

                    coordenadas.append([z, x, y])

                elif tab[z][x][y] == simbot:
                    
                    simbolo = True

                else:
                    simbolo = False

                if vazioCont == 2 and simbolo:

                    escolhido = random.randint(0, len(coordenadas) - 1)
                    escolhidoX = coordenadas[escolhido][1]
                    escolhidoY = coordenadas[escolhido][2]

                    tab[z][escolhidoX][escolhidoY] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", z + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)
                
                y += 1
            x += 1
        z += 1

    z = 0
    while z < 3 and jogando:

        y = 0
        for y in range(0, 3):

            x = 0
            simbolo = False
            vazioCont = 0
            coordenadas = []

            while x < 3 and jogando:

                if tab[z][x][y] == " ":
                    vazioCont += 1

                    coordenadas.append([z, x, y])

                elif tab[z][x][y] == simbot:
                    
                    simbolo = True

                else:
                    simbolo = False
                

                if vazioCont == 2 and simbolo:

                    escolhido = random.randint(0, len(coordenadas) - 1)
                    escolhidoX = coordenadas[escolhido][1]
                    escolhidoY = coordenadas[escolhido][2]

                    tab[z][escolhidoX][escolhidoY] = simbot
                    jogando = False

                    print("Ele escolheu as coordenadas", z + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)

                x += 1
            y += 1
        z += 1

    z = 0
    while z < 3 and jogando:

        xy = 0
        simbolo = False
        vazioCont = 0
        coordenadas = []

        while xy < 3 and jogando:

            if tab[z][xy][xy] == " ":
                vazioCont += 1

                coordenadas.append([z, xy])

            elif tab[z][xy][xy] == simbot:
                    
                simbolo = True

            else:
                simbolo = False
                

            if vazioCont == 2 and simbolo:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoXY = coordenadas[escolhido][1]

                tab[z][escolhidoXY][escolhidoXY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", z + 1, escolhidoXY + 1, escolhidoXY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            xy += 1
        z += 1

    z = 0
    while z < 3 and jogando:
        
        dif = 0
        simbolo = False
        vazioCont = 0
        coordenadas = []

        while dif < 3 and jogando:

            x = dif
            y = 2 - dif

            if tab[z][x][y] == " ":
                vazioCont += 1

                coordenadas.append([z, x, y])

            elif tab[z][x][y] == simbot:
                    
                simbolo = True

            else:
                simbolo = False
                

            if vazioCont == 2 and simbolo:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoX = coordenadas[escolhido][1]
                escolhidoY = coordenadas[escolhido][2]

                tab[z][escolhidoX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", z + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            dif += 1
        z +=1

    return jogando

# A mesma coisa, mas envolvendo mais de uma camada z.
## The same thing, but involving more than one z layer.
def criarSequ2(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    x = 0
    while x < 3 and jogando:

        y = 0
        while y < 3 and jogando:

            z = 0
            vazioCont = 0
            simbolo = False
            coordenadas = []

            while z < 3 and jogando:

                if tab[z][x][y] == " ":
                    vazioCont += 1
                    coordenadas.append([z, x, y])
            
                elif tab[z][x][y] == simbot:
                    simbolo = True
            
                else:
                    simbolo = False

                if vazioCont == 2 and simbolo:

                    escolhido = random.randint(0, len(coordenadas) - 1)
                    escolhidoZ = coordenadas[escolhido][0]
                    escolhidoX = coordenadas[escolhido][1]
                    escolhidoY = coordenadas[escolhido][2]

                    tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)
                
                z += 1
            y += 1
        x += 1

    x = 0
    while x < 3 and jogando:

        zy = 0
        vazioCont = 0
        simbolo = False
        coordenadas = []

        while zy < 3 and jogando:
            
            if jogando == False:
                break
                    
            if tab[zy][x][zy] == " ":
                vazioCont += 1
                coordenadas.append([zy, x])

            elif tab[zy][x][zy] == simbot:
                simbolo = True

            else:
                simbolo = False
                
            if vazioCont == 2 and simbolo:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZY = coordenadas[escolhido][0]
                escolhidoX = coordenadas[escolhido][1]

                tab[escolhidoZY][escolhidoX][escolhidoZY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZY + 1, escolhidoX + 1, escolhidoZY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)

            zy += 1
        x += 1

    x = 0
    while x < 3 and jogando:

        dif = 0
        vazioCont = 0
        simbolo = False
        coordenadas = []

        while dif < 3 and jogando:
            
            z = dif
            y = 2 - dif
                    
            if tab[z][x][y] == " ":
                vazioCont += 1
                coordenadas.append([z, x, y])

            elif tab[z][x][y] == simbot:
                simbolo = True

            else:
                simbolo = False
                
            if vazioCont == 2 and simbolo:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZ = coordenadas[escolhido][0]
                escolhidoX = coordenadas[escolhido][1]
                escolhidoY = coordenadas[escolhido][2]

                tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            dif += 1
        x += 1

    y = 0
    while  y < 3 and jogando:

        zx = 0
        vazioCont = 0
        simbolo = False
        coordenadas = []

        while zx < 3 and jogando:
            
            if tab[zx][zx][y] == " ":
                vazioCont += 1
                coordenadas.append([zx, y])

            elif tab[zx][zx][y] == simbot:
                simbolo = True

            else:
                simbolo = False
                
            if vazioCont == 2 and simbolo:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZX = coordenadas[escolhido][0]
                escolhidoY = coordenadas[escolhido][1]

                tab[escolhidoZX][escolhidoZX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZX + 1, escolhidoZX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            zx += 1
        y += 1

    y = 0
    while y < 3 and jogando:

        dif = 0
        vazioCont = 0
        simbolo = False
        coordenadas = []

        while dif < 3 and jogando:
            
            z = dif
            x = 2 - dif
                    
            if tab[z][x][y] == " ":
                vazioCont += 1
                coordenadas.append([z, x, y])

            elif tab[z][x][y] == simbot:
                simbolo = True

            else:
                simbolo = False
                
            if vazioCont == 2 and simbolo:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZ = coordenadas[escolhido][0]
                escolhidoX = coordenadas[escolhido][1]
                escolhidoY = coordenadas[escolhido][2]

                tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)

            dif += 1
        y += 1




    vazioCont = 0
    simbolo = False
    coordenadas = []

    xyz = 0
    while xyz < 3 and jogando:
                    
        if tab[xyz][xyz][xyz] == " ":
            vazioCont += 1
            coordenadas.append(xyz)

        elif tab[xyz][xyz][xyz] == simbot:
            simbolo = True

        else:
            simbolo = False
                
        if vazioCont == 2 and simbolo:

            escolhidoXYZ = coordenadas[random.randint(0, len(coordenadas) - 1)]

            tab[escolhidoXYZ][escolhidoXYZ][escolhidoXYZ] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoXYZ + 1, escolhidoXYZ + 1, escolhidoXYZ + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        xyz += 1

    vazioCont = 0
    simbolo = False
    coordenadas = []

    
    dif = 0
    while dif < 3 and jogando:

        x = 2 - dif
        zy = dif
                    
        if tab[zy][x][zy] == " ":
            vazioCont += 1
            coordenadas.append([zy, x])

        elif tab[zy][x][zy] == simbot:
            simbolo = True

        else:
            simbolo = False
                
        if vazioCont == 2 and simbolo:

            escolhido = random.randint(0, len(coordenadas) - 1)
            escolhidoZY = coordenadas[escolhido][0]
            escolhidoX = coordenadas[escolhido][1]

            tab[escolhidoZY][escolhidoX][escolhidoZY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoZY + 1, escolhidoX + 1, escolhidoZY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        dif += 1 

    vazioCont = 0
    simbolo = False
    coordenadas = []

    
    dif = 0
    while dif < 3 and jogando:

        y = 2 - dif
        zx = dif

        if tab[zx][zx][y] == " ":
            vazioCont += 1
            coordenadas.append([zx, y])

        elif tab[zx][zx][y] == simbot:
            simbolo = True

        else:
            simbolo = False
                
        if vazioCont == 2 and simbolo:

            escolhido = random.randint(0, len(coordenadas) - 1)
            escolhidoZX = coordenadas[escolhido][0]
            escolhidoY = coordenadas[escolhido][1]

            tab[escolhidoZX][escolhidoZX][escolhidoY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoZX + 1, escolhidoZX + 1, escolhidoY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        dif += 1

    vazioCont = 0
    simbolo = False
    coordenadas = []

    
    dif = 0
    while dif < 3 and jogando:

        z = 2 - dif
        xy = dif

        if tab[z][xy][xy] == " ":
            vazioCont += 1
            coordenadas.append([z, xy])

        elif tab[z][xy][xy] == simbot:
            simbolo = True

        else:
            simbolo = False
                
        if vazioCont == 2 and simbolo:

            escolhido = random.randint(0, len(coordenadas) - 1)
            escolhidoZ = coordenadas[escolhido][0]
            escolhidoXY = coordenadas[escolhido][1]

            tab[escolhidoZ][escolhidoXY][escolhidoXY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoXY + 1, escolhidoXY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)  

        dif += 1  

    return jogando

# Verifica por sequências de três espaços vazios que não atravessam camadas para o bot colocar seu símbolo.
## Checks for a sequence with 3 empty spaces and doesn't involve more than one z layer to play.
def jogarEmVazio1(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    # Verifica por linhas vazias.
    z = 0
    while z < 3 and jogando:

        x = 0
        while x < 3 and jogando:

            y = 0
            vazioCont = 0
            coordenadas = []

            while y < 3 and jogando:

                if tab[z][x][y] == " ":
                    vazioCont += 1
                    coordenadas.append([z, x, y])
                
                if vazioCont == 3:
                    escolhido = random.randint(0, len(coordenadas) - 1)
                    escolhidoZ = coordenadas[escolhido][0]
                    escolhidoX = coordenadas[escolhido][1]
                    escolhidoY = coordenadas[escolhido][2]

                    tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)
                
                y += 1
            x += 1 
        z += 1

    # Verifica por colunas vazias.
    z = 0
    while z < 3 and jogando:

        y = 0
        while y < 3 and jogando:

            x = 0
            vazioCont = 0
            coordenadas = []

            while x < 3 and jogando:

                if tab[z][x][y] == " ":
                    vazioCont += 1

                    coordenadas.append([z, x, y])

                if vazioCont == 3:

                    escolhido = random.randint(0, len(coordenadas) - 1)
                    escolhidoZ = coordenadas[escolhido][0]
                    escolhidoX = coordenadas[escolhido][1]
                    escolhidoY = coordenadas[escolhido][2]

                    tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                    jogando = False

                    print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)
                
                x += 1
            y += 1
        z += 1

    # Verifica se a diagonal principal é vazia.
    z = 0
    while z < 3 and jogando:

        xy = 0
        vazioCont = 0
        coordenadas = []

        while xy < 3 and jogando:

            if tab[z][xy][xy] == " ":
                vazioCont += 1

                coordenadas.append([z, xy])         

            if vazioCont == 3:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZ = coordenadas[escolhido][1]
                escolhidoXY = coordenadas[escolhido][1]

                tab[escolhidoZ][escolhidoXY][escolhidoXY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoXY + 1, escolhidoXY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            xy += 1
        z += 1

    # Verifica se diagonal secundária é vazia.
    z = 0
    while z < 3 and jogando:

        dif = 0
        vazioCont = 0
        coordenadas = []

        while dif < 3 and jogando:

            x = dif
            y = 2 - dif

            if tab[z][x][y] == " ":
                vazioCont += 1

                coordenadas.append([z, x, y])

            if vazioCont == 3:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZ = coordenadas[escolhido][0]
                escolhidoX = coordenadas[escolhido][1]
                escolhidoY = coordenadas[escolhido][2]

                tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            dif += 1
        z += 1

    return jogando

# A mesma coisa, mas envolvendo mais de uma camada z.
## The same thing, but involving more than one z layer.
def jogarEmVazio2(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    x = 0
    while x < 3 and jogando:

        y = 0
        while y < 3 and jogando:
            
            z = 0
            vazioCont = 0
            coordenadas = []

            while z < 3 and jogando:

                if tab[z][x][y] == " ":
                    vazioCont += 1
                    coordenadas.append([z, x, y])

                if vazioCont == 3:

                    escolhido = random.randint(0, len(coordenadas) - 1)
                    escolhidoZ = coordenadas[escolhido][0]
                    escolhidoX = coordenadas[escolhido][1]
                    escolhidoY = coordenadas[escolhido][2]

                    tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                    jogando = False
                    
                    print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                    player(tab, l, scoreBot, scorePlayer)
                
                z += 1
            y += 1
        x += 1 

    x = 0
    while x < 3 and jogando:

        zy = 0
        vazioCont = 0
        coordenadas = []

        while zy < 3 and jogando:

            if tab[zy][x][zy] == " ":
                vazioCont += 1
                coordenadas.append([zy, x])
                
            if vazioCont == 3:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZY = coordenadas[escolhido][0]
                escolhidoX = coordenadas[escolhido][1]

                tab[escolhidoZY][escolhidoX][escolhidoZY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZY + 1, escolhidoX + 1, escolhidoZY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            zy += 1
        x += 1

    x = 0
    while x < 3 and jogando:

        dif = 0
        vazioCont = 0
        coordenadas = []

        while dif < 3 and jogando:
            
            z = dif
            y = 2 - dif

            if tab[z][x][y] == " ":
                vazioCont += 1
                coordenadas.append([z, x, y])
                
            if vazioCont == 3:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZ = coordenadas[escolhido][0]
                escolhidoX = coordenadas[escolhido][1]
                escolhidoY = coordenadas[escolhido][2]

                tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            dif += 1
        x += 1

    y = 0
    while y < 3 and jogando:

        zx = 0
        vazioCont = 0
        coordenadas = []

       
        while zx < 3 and jogando:

            if tab[zx][zx][y] == " ":
                vazioCont += 1
                coordenadas.append([zx, y])
                
            if vazioCont == 3:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZX = coordenadas[escolhido][0]
                escolhidoY = coordenadas[escolhido][1]

                tab[escolhidoZX][escolhidoZX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZX + 1, escolhidoZX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            zx += 1
        y += 1           

    y = 0
    while y < 3 and jogando:
        
        dif = 0
        vazioCont = 0
        coordenadas = []

        while dif < 3 and jogando:
            
            z = dif
            x = 2 - dif

            if tab[z][x][y] == " ":
                vazioCont += 1
                coordenadas.append([z, x, y])
                
            if vazioCont == 3:

                escolhido = random.randint(0, len(coordenadas) - 1)
                escolhidoZ = coordenadas[escolhido][0]
                escolhidoX = coordenadas[escolhido][1]
                escolhidoY = coordenadas[escolhido][2]

                tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
                jogando = False
                
                print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoX + 1, escolhidoY + 1, "\n")
                player(tab, l, scoreBot, scorePlayer)
            
            dif += 1
        y += 1



    vazioCont = 0
    coordenadas = []

    xyz = 0
    while xyz < 3 and jogando:
 
        if tab[xyz][xyz][xyz] == " ":
            vazioCont += 1
            coordenadas.append(xyz)
                
        if vazioCont == 3:

            escolhidoXYZ = coordenadas[random.randint(0, len(coordenadas) - 1)]

            tab[escolhidoXYZ][escolhidoXYZ][escolhidoXYZ] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoXYZ + 1, escolhidoXYZ + 1, escolhidoXYZ + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)

        xyz += 1

    vazioCont = 0
    coordenadas = []

    dif = 0
    while dif < 3 and jogando:

        x = 2 - dif
        zy = dif
                    
        if tab[zy][x][zy] == " ":
            vazioCont += 1
            coordenadas.append([zy, x])
                
        if vazioCont == 3:

            escolhido = random.randint(0, len(coordenadas) - 1)
            escolhidoZY = coordenadas[escolhido][0]
            escolhidoX = coordenadas[escolhido][1]

            tab[escolhidoZY][escolhidoX][escolhidoZY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoZY + 1, escolhidoX + 1, escolhidoZY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        dif += 1

    vazioCont = 0
    coordenadas = []

    dif = 0
    while dif < 3 and jogando:

        y = 2 - dif
        zx = dif

        if tab[zx][zx][y] == " ":
            vazioCont += 1
            coordenadas.append([zx, y])
                
        if vazioCont == 3:

            escolhido = random.randint(0, len(coordenadas) - 1)
            escolhidoZX = coordenadas[escolhido][0]
            escolhidoY = coordenadas[escolhido][1]

            tab[escolhidoZX][escolhidoZX][escolhidoY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoZX + 1, escolhidoZX + 1, escolhidoY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)
        
        dif += 1

    vazioCont = 0
    coordenadas = []

    dif = 0
    while dif < 3 and jogando:

        z = 2 - dif
        xy = dif

        if tab[z][xy][xy] == " ":
            vazioCont += 1
            coordenadas.append([z, xy])
                
        if vazioCont == 3:

            escolhido = random.randint(0, len(coordenadas) - 1)
            escolhidoZ = coordenadas[escolhido][0]
            escolhidoXY = coordenadas[escolhido][1]

            tab[escolhidoZ][escolhidoXY][escolhidoXY] = simbot
            jogando = False
            
            print("Ele escolheu as coordenadas", escolhidoZ + 1, escolhidoXY + 1, escolhidoXY + 1, "\n")
            player(tab, l, scoreBot, scorePlayer)  

        dif += 1  

    return jogando

# Joga em qualquer espaço vazio.
## Plays in any random empty space.
def jogarQualquer(tab, simbot, l, scoreBot, scorePlayer):

    jogando = True

    coordenadas = []

    for z in range (0, 3):

        for x in range (0, 3):

            for y in range(0, 3):

                if tab[z][x][y] == " ":

                    coordenadas.append([z, x, y])
    
    escolhido = random.randint(0, len(coordenadas) - 1)
    escolhidoZ = coordenadas[escolhido][0]
    escolhidoX = coordenadas[escolhido][1]
    escolhidoY = coordenadas[escolhido][2]

    tab[escolhidoZ][escolhidoX][escolhidoY] = simbot
    jogando = False

    verificarEmpate(tab, l, scoreBot, scorePlayer, True)



# Verificação de resultado:
## Algorithms that check the result:



# Verifica se o tabuleiro está cheio e se houve empate.
## Checks if the matrix is full and if there is a stalemate.
def verificarEmpate(tab, k, scoreBot, scorePlayer, bot):

    cheio = True
    z = 0
    while cheio and z < 3:
        x = 0
        while cheio and x < 3:
            y = 0
            while cheio and y < 3:
                if tab[z][x][y] == " ":
                    cheio = False
                y += 1
            x += 1
        z += 1

    if bot and cheio:

        telaFinal(tab, "Ninguém", scoreBot, scorePlayer)

    elif bot and not cheio:

        player(tab, k, scoreBot, scorePlayer)

    else:
        verificarVitoria(tab, k, scoreBot, scorePlayer, cheio)

# Verifica se o jogador venceu.
## Checks if the player won.
def verificarVitoria(tab, k, scoreBot, scorePlayer, cheio):

    venceu = False

    z = 0
    while (not venceu) and z < 3:
        x = 0
        while (not venceu) and x < 3:
            y = 0
            cont = 0
            while (not venceu) and y < 3:
                if tab[z][x][y] == k:
                    cont += 1
                
                if cont == 3:
                    venceu = True
                y += 1
            x += 1
        z += 1

    z = 0
    while (not venceu) and z < 3:
        y = 0
        while (not venceu) and y < 3:
            x = 0
            cont = 0
            while (not venceu) and x < 3:
                if tab[z][x][y] == k:
                    cont += 1
                
                if cont == 3:
                    venceu = True
                
                x += 1
            y += 1
        z += 1

    z = 0
    while (not venceu) and z < 3:
        xy = 0
        cont = 0
        while (not venceu) and xy < 3:
            if tab[z][xy][xy] == k:
                cont += 1
                
            if cont == 3:
                venceu = True
                
            xy += 1
        z += 1

    z = 0
    while (not venceu) and z < 3:
        dif = 0
        cont = 0
        while (not venceu) and dif < 3:
            x = dif
            y = 2 - dif
            if tab[z][x][y] == k:
                cont += 1
                
            if cont == 3:
                venceu = True
                
            dif += 1
        z += 1

    x = 0
    while (not venceu) and x < 3:
        y = 0
        while (not venceu) and y < 3:
            z = 0
            cont = 0
            while (not venceu) and z < 3:
                if tab[z][x][y] == k:
                    cont += 1
                
                if cont == 3:
                    venceu = True
                
                z += 1
            y += 1
        x += 1

    x = 0
    while (not venceu) and x < 3:
        zy = 0
        cont = 0
        while (not venceu) and zy < 3:
            if tab[zy][x][zy] == k:
                cont += 1
                
            if cont == 3:
                venceu = True
                
            zy += 1
        x += 1

    x = 0
    while (not venceu) and x < 3:
        dif = 0
        cont = 0
        while (not venceu) and dif < 3:
            z = dif
            y = 2 - dif
            if tab[z][x][y] == k:
                cont += 1
            if cont == 3:
                venceu = True
                
            dif += 1
        x += 1

    y = 0
    while (not venceu) and y < 3:
        zx = 0
        cont = 0
        while (not venceu) and zx < 3:
            if tab[zx][zx][y] == k:
                cont += 1
                
            if cont == 3:
                venceu = True
                
            zx += 1
        y += 1

    y = 0
    while (not venceu) and y < 3:
        dif = 0
        cont = 0
        while (not venceu) and dif < 3:
            z = dif
            x = 2 - dif
            if tab[z][x][y] == k:
                cont += 1
                
            if cont == 3:
                venceu = True
                
            dif += 1
        y += 1

    # Verifica por situações de vitória do player nas diagonais espaciais do tabuleiro.
    ## Checks for player victory situations on the 3D matrix diagonals.
    ##1
    if (not venceu):
        cont = 0
        xyz = 0
        while xyz < 3:
            if tab[xyz][xyz][xyz] == k:
                cont += 1
            xyz += 1
    
        if cont == 3:
            venceu = True

    ##2
    if (not venceu):
        cont = 0
        dif = 0
        while dif < 3:
            x = 2 - dif
            zy = dif
            if tab[zy][x][zy] == k:
                cont += 1
            dif += 1
    
        if cont == 3:
            venceu = True

    ##3
    if (not venceu):
        cont = 0
        dif = 0
        while dif < 3:
            y = 2 - dif
            zx = dif
            if tab[zx][zx][y] == k:
                cont += 1
            dif += 1
    
        if cont == 3:
            venceu = True

    ##4
    if (not venceu):
        cont = 0
        dif = 0
        while dif < 3:
            z = 2 - dif
            xy = dif
            if tab[z][xy][xy] == k:
                cont += 1
            dif += 1
    
        if cont == 3:
            venceu = True

    if venceu:
        telaFinal(tab, "Jogador", scoreBot, scorePlayer)

    elif (not venceu) and (not cheio):
        bot(tab, k, scoreBot, scorePlayer)

    elif (not venceu) and cheio:
        telaFinal(tab, "Ninguém", scoreBot, scorePlayer)


# Cria um tabuleiro 3x3x3 preenchido com " "
##  Creates a 3x3x3 matrix filled with " "

tabuleiro = [[[" " for i in range(3)] for i in range(3)]for i in range(3)]
game(tabuleiro, 0, 0)