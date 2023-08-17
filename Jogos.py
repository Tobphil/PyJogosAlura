import jogoadivinhacao
import Sorteio


print("  *** Escolha o seu jogo ***")
print("****************************")
print("(1) Adivinhação (2) Sorteio")
jogo = int(input("Escolha o Jogo"))

if (jogo == 1):
    jogoadivinhacao.jogar()
elif (jogo == 2):
    Sorteio.jogar()