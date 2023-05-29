game = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
pontosJogador1=0
pontosJogador2=0
jogadas=0
velha=True
print("---------------REGRAS---------------\n\n-Começa com jogador 1\n-Próxima partida começa com quem perder\n-O jogador que escolher um número errado perderá a vez\n-(x) jogador 1  | (O) jogador 2")
print(f"\n{game[0]}\n{game[1]}\n{game[2]}")

while True:
#   Velha vai ser False quando o jogador ganhar, e ao retornar o loop volta a ser True
    velha=True

    jogar = input("JOGADOR 1 ESCOLHER UM NÚMERO: ")
    for x in range(3):
        if jogar in game[x]:
            for y in range(3):
                if jogar == game[x][y]:
                    game[x][y]='x'
    print(f"\n{game[0]}\n{game[1]}\n{game[2]}")

    match game[0]:
        case ['x','x','x']:
            print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
            print("JOGADOR 1 VENCEU!")
            pontosJogador1+=1
            jogadas=0
            velha=False
            game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    match game[1]:
        case ['x', 'x', 'x']:
            print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
            print("JOGADOR 1 VENCEU!")
            pontosJogador1+=1
            jogadas=0
            velha=False
            game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")

    match game[2]:
        case ['x', 'x', 'x']:
            print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
            print("JOGADOR 1 VENCEU!")
            pontosJogador1+=1
            jogadas=0
            velha=False
            game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")

    if game[0][0]=='x' and game[1][1]=='x' and game[2][2]=='x':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 1 VENCEU!")
        pontosJogador1+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    elif game[0][2] == 'x' and game[1][1] == 'x' and game[2][0] == 'x':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 1 VENCEU!")
        pontosJogador1+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")

    elif game[0][0] == 'x' and game[1][0] == 'x' and game[2][0] == 'x':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 1 VENCEU!")
        pontosJogador1+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    elif game[0][1] == 'x' and game[1][1] == 'x' and game[2][2] == 'x':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 1 VENCEU!")
        pontosJogador1+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    elif game[0][2] == 'x' and game[1][2] == 'x' and game[2][2] == 'x':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 1 VENCEU!")
        pontosJogador1+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    else:
        if velha==True:
            jogadas+=1

    if jogadas==9 and velha==True:
        jogadas=0
        velha=False
        print("DEU VELHA!")
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")

    jogar = input("JOGADOR 2 ESCOLHER UM NÚMERO: ")
    for x in range(3):
        if jogar in game[x]:
            for y in range(3):
                if jogar == game[x][y]:
                    game[x][y]='O'
    print(f"\n{game[0]}\n{game[1]}\n{game[2]}")


    match game[0]:
        case ['O','O','O']:
            print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
            print("JOGADOR 2 VENCEU!")
            pontosJogador2+=1
            jogadas=0
            velha=False
            game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    match game[1]:
        case ['O', 'O', 'O']:
            print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
            print("JOGADOR 2 VENCEU!")
            pontosJogador2+=1
            jogadas=0
            velha=False
            game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    match game[2]:
        case ['O', 'O', 'O']:
            print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
            print("JOGADOR 2 VENCEU!")
            pontosJogador2+=1
            jogadas=0
            velha=False
            game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")

    if game[0][0]=='O' and game[1][1]=='O' and game[2][2]=='O':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 2 VENCEU!")
        pontosJogador2+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    elif game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 2 VENCEU!")
        pontosJogador2+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    elif game[0][0] == 'O' and game[1][0] == 'O' and game[2][0] == 'O':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 2 VENCEU!")
        pontosJogador2+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    elif game[0][1] == 'O' and game[1][1] == 'O' and game[2][1] == 'O':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 2 VENCEU!")
        pontosJogador2+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    elif game[0][2] == 'O' and game[1][2] == 'O' and game[2][2] == 'O':
        print(f"\n{game[0]}\n{game[1]}\n{game[2]}")
        print("JOGADOR 2 VENCEU!")
        pontosJogador2+=1
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")
    else:
        if velha==True:
            jogadas+=1

    if jogadas==9 and velha == True:
        print("\nDEU VELHA!\n")
        jogadas=0
        velha=False
        game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {pontosJogador1}|{pontosJogador2}   Jogador 2\n\n{game[0]}\n{game[1]}\n{game[2]}")