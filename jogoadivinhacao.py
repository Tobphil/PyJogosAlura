print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou ", chute)
acertou = numero_secreto == chute
maior = numero_secreto < chute

if(acertou):
    print ("você acertou")
    print("Finalizar")
else:
    print("você errou")
    if(maior):
        print("Chute maior que numero secreto")
    else:
        print("Chute menor que numero secreto")