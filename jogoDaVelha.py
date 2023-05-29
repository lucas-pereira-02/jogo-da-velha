class Atributos():
    def __init__(self):
        self.game=[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.pontosJogador1=0
        self.pontosJogador2=0
        self.jogadas=0
        self.velha=True
    def imprimirGrade(self):
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")

class Jogo(Atributos):
    def __init__(self):
        super().__init__()
    def vitoria(self):
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")
        print("JOGADOR 1 VENCEU!")
        self.pontosJogador1 += 1
        self.jogadas = 0
        self.velha = False
        self.game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {self.pontosJogador1}|{self.pontosJogador2}   Jogador 2\n\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")
        return self.pontosJogador1, self.jogadas, self.velha, self.game

    def jogar(self):
        jogar = input("JOGADOR 1 ESCOLHER UM NÚMERO: ")
        for x in range(3):
            if jogar in self.game[x]:
                for y in range(3):
                    if jogar == self.game[x][y]:
                        self.game[x][y] = 'x'
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")

    def velhaFalse(self):
        self.velha=True
        return self.velha

    def verificar(self):
        match self.game[0]:
            case ['x', 'x', 'x']:
                Jogo.vitoria(self)
print("---------------REGRAS---------------\n\n-Começa com jogador 1\n-Próxima partida começa com quem perder\n-O jogador que escolher um número errado perderá a vez\n-(x) jogador 1  | (O) jogador 2")
atributos = Atributos()
jogo=Jogo()
atributos.imprimirGrade()
while True:
#   Velha vai ser False quando o jogador ganhar, e ao retornar o loop volta a ser True
    jogo.velhaFalse()

    jogo.jogar()
    jogo.verificar()



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