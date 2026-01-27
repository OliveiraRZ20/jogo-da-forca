# imports internos

# imports externos

REGRAS: str = """
|+--------------------------------------------------------------------------------------+|
|                                    REGRAS                                              |
|+--------------------------------------------------------------------------------------+|
| - O jogo consiste no usuário adivinhar uma palavra escolhida aleatoriamente            |
| - O jogador deve escolher entre tentar descobrir uma letra ou a palavra inteira.       |
| - O jogador perde se errar 6 vezes, completando o boneco da forca.                     |
| - O jogador vence se conseguir desvendar todas as letras ou adivinhar a palavra        |
|+--------------------------------------------------------------------------------------+|
"""

MENU: str = """
|+-----------------------------+|
|             MENU              |
|+-----------------------------+|
| 1. Iniciar um novo jogo       |
| 2. Ver as regras do jogo      |
| 3. Sair do jogo               |
|+-----------------------------+|
"""

class Menu:
    
    @staticmethod
    def exibir_regras():
        print(REGRAS)
    
    @staticmethod
    def exibir_menu():
        print(MENU)
