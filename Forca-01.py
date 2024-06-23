# pseudocódigo para programar um jogo da forca em terminal

# DEFINICÕES (BACK END)
# definir lista de palavras
# escolher palavra aleatoria dessa lista
# lista vazia para armazenamento de letras adivinhadas
# definir número máximo de tentativas permitidas
# checar se a letra digitada pelo usuario é parte da palavra escolhida

# EXECUÇÃO (FRONT END)
# print "Bem vindo ao jogo da forca"
# print "Advinhe a palavra abaixo: "
# desenhar imagens na tela

import random
from os import system, name

def limpa_tela():
    if name ==  "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def game():
    
    # limpar tela no inicio do game
    limpa_tela()
    
    # mensagem inicial
    print("\nBem vindo ao jogo da forca do Lucca")
    print("Tente adivinhar a palavra escolhida aleatoriamente, heheheheheeh...\n")
    
    # lista de palavras 
    palavras = ["banana", "abacate", "abacaxi", "uva", "morango", "laranja", "kiwi"]
    
    # escolher palavra 
    palavra = random.choice(palavras)
    
    # criar os underlines para representar letras descobertas
    letras_descobertas = ["_" for letra in palavra]
    
    # número de chances
    chances = 6
    
    # lista de letras erradas
    letras_erradas = []
    
    # loop para enquanto as chances forem maiores que 0
    while chances > 0:
        print(" ".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        print(f"Letras erradas: ", " ".join(letras_erradas))
        
        # tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        
        if tentativa == palavra:
            print(f"\nParabéns, voce acertou a palavra direto, a palavra era: {palavra}")
            break
        
        if tentativa in palavra:
            print("Boa, acertou a letra")
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            print("Putz, que pena, errou...")
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print(f"\nParabéns, você venceu, a palavra era: {palavra}")
            break
    if "_" in letras_descobertas:
        print(f"\nVocê perdeu, a palavra eraL {palavra}")

game()
print("GG boys")


