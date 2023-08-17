import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = round(random.randrange(1, 101))
    print("Número randomico =", numero_secreto)

    # definindo nível dificuldade INICIO
    total_de_tentativas = 0
    print("Escolha o nível dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Digite: "))
    if (dificuldade == 1):
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    elif (dificuldade == 3):
        total_de_tentativas = 5
    else:
        print("Opção inválida") #vai automaticamente para o fim (não atende FOR)
        pontos = 0
    # definindo nível dificuldade FIM

    #Pontuação jogador que diminui a cada tentativa. Inicio em 100, muda com grau dificuldade
    pontos = 100

    for rodada in range(1, total_de_tentativas + 1):

        #print("Tentativa: ", rodada, " de ", total_de_tentativas)
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu número entre 1 e 100: "))
        acertou = numero_secreto == chute
        maior = numero_secreto < chute

        #testa número digitado INICIO
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue  # volta para rodada/ continua execução
        if (acertou):
            print("você acertou")
            break  # sai do laço FOR ou While
        if (maior):
            print("Você errou! Chute MAIOR que número secreto")
            pontos = (pontos - (pontos // total_de_tentativas))
        else:
            print("Você errou! Chute MENOR que número secreto")
            pontos = (pontos - (pontos // total_de_tentativas))

    print("  ***  FIM  *** ")
    print(" **** Pontos *** {:2d}".format(pontos))

if(__name__ == "__main__"):
    jogar()