class Atributos():
    def __init__(self):
        self.game=[['1', '2', '3'],
                   ['4', '5', '6'],
                   ['7', '8', '9']]
        self.pontosJogador1=0
        self.pontosJogador2=0
        self.jogadas=0
        self.velha=True
        self.numero=0
    def imprimirGrade(self):
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")

class Jogo(Atributos):
    def __init__(self):
        super().__init__()
    def jogada1(self):

        numero = input("JOGADOR 1 ESCOLHA UM NÚMERO: ")
        for x in range(3):
            if numero in self.game[x]:
                for y in range(3):
                    if numero == self.game[x][y]:
                        self.game[x][y] = 'X'
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")

    def verificar1(self):
        if self.game[0] == ['X', 'X', 'X']:
            Jogo.vitoria1(self)
        elif self.game[1] == ['X', 'X', 'X']:
            Jogo.vitoria1(self)
        elif self.game[2] == ['X', 'X', 'X']:
            Jogo.vitoria1(self)
        elif self.game[0][0] == 'X' and self.game[1][1] == 'X' and self.game[2][2] == 'X':
            Jogo.vitoria1(self)
        elif self.game[0][0] == 'X' and self.game[1][0] == 'X' and self.game[2][0] == 'X':
            Jogo.vitoria1(self)
        elif self.game[0][1] == 'X' and self.game[1][1] == 'X' and self.game[2][1] == 'X':
            Jogo.vitoria1(self)
        elif self.game[0][2] == 'X' and self.game[1][2] == 'X' and self.game[2][2] == 'X':
            Jogo.vitoria1(self)
        elif self.game[0][2] == 'X' and self.game[1][1] == 'X' and self.game[2][0] == 'X':
            Jogo.vitoria1(self)
        else:
            self.velha=True
            self.jogadas+=1
            Jogo.verificarVelha(self)

    def imprimirJogadas(self):
        print(self.jogadas)

    def jogada2(self):
        numero = input("JOGADOR 2 ESCOLHA UM NÚMERO: ")
        for x in range(3):
            if numero in self.game[x]:
                for y in range(3):
                    if numero == self.game[x][y]:
                        self.game[x][y] = 'O'
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")

    def verificar2(self):
        if self.game[0] == ['O', 'O', 'O']:
            Jogo.vitoria2(self)
        elif self.game[1] == ['O', 'O', 'O']:
            Jogo.vitoria2(self)
        elif self.game[2] == ['O', 'O', 'O']:
            Jogo.vitoria2(self)
        elif self.game[0][0] == 'O' and self.game[1][1] == 'O' and self.game[2][2] == 'O':
            Jogo.vitoria2(self)
        elif self.game[0][0] == 'O' and self.game[1][0] == 'O' and self.game[2][0] == 'O':
            Jogo.vitoria2(self)
        elif self.game[0][1] == 'O' and self.game[1][1] == 'O' and self.game[2][1] == 'O':
            Jogo.vitoria2(self)
        elif self.game[0][2] == 'O' and self.game[1][2] == 'O' and self.game[2][2] == 'O':
            Jogo.vitoria2(self)
        elif self.game[0][2] == 'O' and self.game[1][1] == 'O' and self.game[2][0] == 'O':
            Jogo.vitoria2(self)
        else:
            self.velha=True
            self.jogadas+=1
            Jogo.verificarVelha(self)
    def verificarVelha(self):
        if self.jogadas == 9 and self.velha == True:
            self.jogadas = 0
            self.velha = False
            print("DEU VELHA!")
            self.game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print(f"Jogador 1   {self.pontosJogador1}|{self.pontosJogador2}   Jogador 2\n\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")
            return self.jogadas, self.velha, self.game
    def vitoria1(self):
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")
        print("JOGADOR 1 VENCEU!")
        self.pontosJogador1+=1
        self.jogadas=0
        self.velha=False
        self.game=[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {self.pontosJogador1}|{self.pontosJogador2}   Jogador 2\n\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")
        return self.pontosJogador1, self.jogadas, self.velha, self.game

    def vitoria2(self):
        print(f"\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")
        print("JOGADOR 2 VENCEU!")
        self.pontosJogador2+=1
        self.jogadas=0
        self.velha=False
        self.game=[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"Jogador 1   {self.pontosJogador1}|{self.pontosJogador2}   Jogador 2\n\n{self.game[0]}\n{self.game[1]}\n{self.game[2]}")
        return self.pontosJogador2, self.jogadas, self.velha, self.game
    def velhaTrue(self):
        self.velha=True
        return self.velha
