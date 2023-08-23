def jogar():
    print("********************************")
    print("   Bem vindo ao jogo Forca! ")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False
    tamanho_palavra = len(palavra_secreta)
    continua = 0
    chances = 0
    chances_forca = 6

    #enquanto (true e true)
    while(not enforcou and not acertou and continua < tamanho_palavra and chances < chances_forca):
        chute = input("Qual a letra? ")
        chute = chute.strip() #retira possíveis espaços digitados pelo usuário
        index = 0
        tmp = False
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = chute
                continua = continua + 1
                tmp = True
            index = index + 1
        if (not tmp):
            chances = chances + 1



    print("Fim do jogo!")
   # print(continua, chute, forca)
    print(letras_acertadas)
if(__name__ == "__main__"):
    jogar()