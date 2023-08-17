import random

def jogar():
    print("********************************")
    print("  Bem vindo ao jogo de Sorteio")
    print("********************************")
    numero_sorte = random.randrange(1,4)

    #print(numero_sorte)

    if(numero_sorte == 1):
        print("Vencedor = Paulo")
    elif(numero_sorte == 2):
        print("Vencedor: Juliana")
    elif(numero_sorte == 3):
        print("Vencedor: Tamires")

if(__name__ == "__main__"):
    jogar()