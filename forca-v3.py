# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Classe
class Hangman:

     board = [  # estágio 6 (final)
     """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
           """,
   # estágio 5
   """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
           """,
   # estágio 4
   """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
           """,
   # estágio 3
   """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
           """,
    # estágio 2
   """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
           """ ,
   # estágio 1
   """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
           """,
   # estágio 0
   """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
           """,
    ]

	# Método Construtor
     def __init__(self):
          self.chances = 5
          self.palavras = ["banana", "abacate", "abacaxi", "uva", "morango", "laranja", "kiwi"]
          self.palavra_atual = random.choice(self.palavras)
          self.letras_descobertas = ["_" for letra in self.palavra_atual]
          self.letras_erradas = []
          self.board = Hangman.board
          print("Bem vindo ao jogo da forca do Lucca")
          print("Tente adivinhar a palavra escolhida aleatoriamente, heheheheheeh...")
          print("Jogo inicializado e preparado.")
     
     # Método de limpar a tela
     def limpa_tela(self):
          if name == "nt":
               _ = system("cls")
          else:
               _ = system("clear")
     
	# Método para adivinhar a letra
     def tentativa(self):
          chute = input("digite uma letra ou arrisque adivinhar a palavra toda: ").lower()
          if chute == "exit":
               self.chances = 0
               print("Saindo...")
          elif chute == self.palavra_atual:
               self.letras_descobertas = self.palavra_atual
               print(f"\nParabéns, voce acertou a palavra direto, a palavra era: {self.palavra_atual}")
          elif chute in self.palavra_atual:
               print("Boa, Acertou uma letra.")
               index = 0 
               for letra in self.palavra_atual:
                    if chute == letra:
                         self.letras_descobertas[index] = letra
                    index += 1
          else:
               print(f"Putz, que pena, errou...")
               self.chances -= 1
               for letra in chute:
                    if letra in self.palavra_atual or self.letras_erradas:
                         pass
                    else:
                         self.letras_erradas.append(letra)

	# Método para verificar se o jogo terminou
     def verifica_end(self):
          if self.chances == 0 and "_" in self.letras_descobertas:
               print(f"\nVocê perdeu, a palavra era: {self.palavra_atual}")
               return True
          else:
               return False

	# Método para verificar se o jogador venceu
     def verifica_win(self):
          if self.chances != 0 and "_" not in self.letras_descobertas:
               print(f"\nVocê ganhou!!!, parabéns, a palavra era: {self.palavra_atual}")
               return True
          else:
               return False

	# Método para não mostrar a letra no board
     def mostra_tela(self):
          print(self.board[self.chances+1])
          print(" ".join(self.letras_descobertas))
          print(f"\nChances restantes: {self.chances}")
          print(f"Letras erradas: ", " ".join(self.letras_erradas))
		
	# Método para checar o status do game e imprimir o board na tela


if __name__ == "__main__":
     Game = Hangman()
     while not Game.verifica_end() and not Game.verifica_win():
          Game.limpa_tela()
          Game.mostra_tela()
          Game.tentativa()