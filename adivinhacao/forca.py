import random
from ast import While


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    arquivo = open("palavra.txt","r")
    palavras = []
    

    for linha in arquivo:
        linha = linha.strip()   
        palavras.append(linha)
        

    arquivo.close()
    print(palavras)
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    print(palavra_secreta)

    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)
 
        
    acertou = False
    enforcou = False  
    erros = 0

#Enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip().upper()
        
        index = 0
        if chute in palavra_secreta:

            for letra in palavra_secreta:
                if (chute == letra):
                    print("Encontrei a letra {} na posição {}".format(letra,index))
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            enforcou = erros == 6

        print(letras_acertadas)


    
        

    print("Fim de Jogo")

if (__name__ == '__main__'):    
    jogar()

