print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas+1):
#    print("Tentativa: ", rodada, " de ", total_de_tentativas)
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    acertou = numero_secreto == chute
    maior = numero_secreto < chute

    if(acertou):
        print ("você acertou")
    else:
        print("você errou")
        if(maior):
            print("Chute maior que numero secreto")
        else:
            print("Chute menor que numero secreto")
print("Finalizar")