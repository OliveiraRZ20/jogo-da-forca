from src.Game import Game
from src.terminal import cls, pause

def main() -> None:
    game = Game()
    while True:
        cls()
        game.mostrar_status_atual()
        game.fazer_tentativa()
        if game.checar_finalizacao():
            break
        pause()


if __name__ == '__main__':
    main()
