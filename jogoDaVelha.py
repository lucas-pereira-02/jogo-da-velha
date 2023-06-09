import funcoesJogoDaVelha
from funcoesJogoDaVelha import Atributos
from funcoesJogoDaVelha import Jogo
print("---------------REGRAS---------------\n\n-Começa com jogador 1\n-Próxima partida começa com quem perder\n-O jogador que escolher um número errado perderá a vez\n-(x) jogador 1  | (O) jogador 2")
atributos = Atributos()
jogo=Jogo()
atributos.imprimirGrade()
while True:
#   Velha vai ser False quando o jogador ganhar, e ao retornar o loop volta a ser True
    jogo.velhaTrue()

    jogo.jogada1()
    jogo.verificar1()
    jogo.jogada2()
    jogo.verificar2()