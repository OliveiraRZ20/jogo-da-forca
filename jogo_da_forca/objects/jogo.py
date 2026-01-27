# imports internos
from jogo_da_forca.objects import Hangman
from jogo_da_forca.objects.banco_de_palavras import palavras
from jogo_da_forca.utils.logger import informar, alertar, confirmar
from jogo_da_forca.utils.user_input import ler_tentativa


# imports externos
from random import choice



class Jogo:
    def __init__(self, hangman: Hangman):
        self.hangman: Hangman = hangman
        self.palavra_alvo: str = choice(palavras)
        self.letras_descobertas: list[str] = []
        self.letras_erradas: list[str] = []
        self.palavras_erradas: list[str] = []
    
    def exibir_status(self):
        # 1. Exibe a forca
        print(self.hangman.get_pose())
        # 2. Exibe a palavra secreta com as letras descobertas
        print(f"Palavra: {' '.join([letra if letra in self.letras_descobertas else '_' for letra in self.palavra_alvo])}")
        # 3. Exibe lista de letras erradas digitadas
        print(f"Letras erradas: {', '.join(self.letras_erradas)}")
        # 4. Exibe lista de palavras erradas digitadas
        print(f"Palavras erradas: {', '.join(self.palavras_erradas)}")
    
    def turno(self):
        # Captura entrada do usuário
        tentativa: str = ler_tentativa("Digite uma letra ou palavra: ")
        
        match len(tentativa):
            case 1:
                if tentativa in self.letras_erradas or tentativa in self.letras_descobertas:
                    informar(f"Você já tentou a letra '{tentativa}'. Tente outra.")
                elif tentativa in self.palavra_alvo:
                    self.letras_descobertas.append(tentativa)
                    confirmar(f"Boa! A letra '{tentativa}' está na palavra.")
                else:
                    self.letras_erradas.append(tentativa)
                    self.hangman.errou()
                    alertar(f"A letra '{tentativa}' não está na palavra.")
            case _:
                if tentativa in self.palavras_erradas:
                    informar(f"Você já tentou a palavra '{tentativa}'. Tente outra.")
                elif tentativa == self.palavra_alvo:
                    self.letras_descobertas = list(self.palavra_alvo)
                    confirmar(f"Parabéns! Você acertou a palavra {tentativa!r}.")
                else:
                    self.palavras_erradas.append(tentativa)
                    self.hangman.errou()
                    alertar(f"A palavra {tentativa!r} está incorreta.")
    
    def checar_finalizacao(self) -> tuple[bool, str, str]:
        if self.hangman.erros == 6:
            return (True, 'derrota', f"Você perdeu! A palavra era '{self.palavra_alvo}'.")
        elif "".join(self.letras_descobertas) == self.palavra_alvo:
            return (True,'vitoria', "Parabéns! Você venceu!")
        else:
            return (False, "", "")