import random

def jogar():

    mensagem_boas_vindas()
    palavra_secreta = carrega_arquivo_palavra_secreta()
        #palavra_secreta é uma variável interna da função carrega_arquivo, então criamos aqui novamente para o código principal (main)
        #palavra_secreta = "banana".upper() ## alterado para leitura arquivo
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)


    enforcou = False
    acertou = False
    erros = 0

    #enquanto (true e true)
    while(not enforcou and not acertou ):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,palavra_secreta,letras_acertadas) #passando as variáveis que a função pede_chute precisa, pois não foram criadas dentro da função. Sao passadas pela chamada da função
        else:
            erros += 1
            print("Faltam {} tentativas".format(6-erros))
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()


def mensagem_boas_vindas():
    print("********************************")
    print("   Bem vindo ao jogo Forca! ")
    print("********************************")

def carrega_arquivo_palavra_secreta()
    arquivo = open("palavras.txt", "r")  # abre arquivo.txt para leitura
    palavras = []
    for linha_arquivo in arquivo:
        linha_arquivo = linha_arquivo.strip()  # lê cada linha e limpa caracteres em branco e especiais (\n)
        palavras.append(linha_arquivo)  # adiciona na lista palavras todas as linhas
    arquivo.close()  # fecha arquivo.txt
    # escolhe aleatoreamente a palavra
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[
        numero].upper()  # define palavra secreta = lista palavras na posição/linha "número" definida aleatoreamente e deixa tudo maiúsculo
    return palavra_secreta

def inicializa_letras_acertadas(palavra)
    return ["_" for letra in
            palavra]  # preenche a 'lista' com "_" para cada letra da palavra secreta; #já retorna o valor que queremos, não precisa criar variável
    # letras_acertadas = ["_","_","_","_","_","_"]

def pede_chute():
    chute = input("Qual a letra? ").strip().upper())  # retira espaços digitados pelo usuário
    return chute

    def marca_chute_correto(chute, palavra_secreta, letras_acertadas):  # recebendo variáreis de onde chama a função
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1

    # podemos usar também outra forma: loop infinito:

    #while (True):

    # (...)

    #if (erros == 6):
    #    break
    #if ("_" not in letras_acertadas):
    #    break
    #print(letras_acertadas)

    # (...)