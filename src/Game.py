from random import choice
from src.hangman import get_hangman_pose
from src.terminal import informar, confirmar, alertar
from src.palavras import palavras

class Game:
    def __init__(self):
        self.palavra_alvo: str = self.escolher_palavra()
        self.letras_descobertas: list[str] = ["_" for _ in self.palavra_alvo]
        self.tentativas_erradas: list[str] = []
        self.erros: int = 0

    @staticmethod
    def escolher_palavra():
        return choice(palavras)

    def mostrar_status_atual(self):
        print(get_hangman_pose(self.erros))
        print(f"Palavra oculta: {" ".join(self.letras_descobertas)}")
        print(f"Tentativas erradas: {", ".join(self.tentativas_erradas)}")

    @staticmethod
    def captar_tentativa() -> str:
        while True:
            tentativa: str = input("Faça sua tentativa:\n> ")
            if tentativa == "":
                alertar(f"Tentativa não contem caracteres: {tentativa!r}")
            elif not tentativa.isalpha():
                alertar(f"Tentativa contém caracteres não alfabéticos: {tentativa!r}: ")
            else:
                return tentativa

    def fazer_tentativa(self):
        tentativa: str = self.captar_tentativa()
        if len(tentativa) == 1:
            if tentativa in self.tentativas_erradas or tentativa in self.letras_descobertas:
                informar("Você já tentou essa letra, vou te dar essa colher de chá")
            elif tentativa in self.palavra_alvo:
                confirmar(f"Parabéns, a palavra oculta contém a letra {tentativa}, continue assim!")
                for i in range(len(self.palavra_alvo)):
                    if self.palavra_alvo[i] == tentativa:
                        self.letras_descobertas[i] = tentativa
            else:
                 informar(f"Infelizmente a palavra oculta não contém a letra {tentativa}, tente novamente")
                 self.erros += 1
                 self.tentativas_erradas.append(tentativa)
        else:
            if tentativa == self.palavra_alvo:
                self.letras_descobertas = list(tentativa)
            else:
                informar("Infelizmente você não acertou a palavra, tente novamente!")
                self.erros += 1
                self.tentativas_erradas.append(tentativa)

    def checar_finalizacao(self) -> bool:
        if "".join(self.letras_descobertas) == self.palavra_alvo:
            confirmar(f"Parabéns, você descobriu a palavra {self.palavra_alvo!r} com um total de {self.erros} erro(s)")
            return True
        if self.erros == 6:
            informar(f"Infelizmente você perdeu. a palavra oculta era {self.palavra_alvo!r}, mais sorte na próxima!")
            return True
        else:
            return False