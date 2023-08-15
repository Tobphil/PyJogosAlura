print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas+1):
#    print("Tentativa: ", rodada, " de ", total_de_tentativas)
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número entre 1 e 100: "))

    acertou = numero_secreto == chute
    maior = numero_secreto < chute
    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue #volta para rodada/ continua execução

    if(acertou):
        print ("você acertou")
        break #sai do laço FOR ou While
    else:
        print("você errou")
        if(maior):
            print("Chute maior que numero secreto")
        else:
            print("Chute menor que numero secreto")
print("Finalizar")