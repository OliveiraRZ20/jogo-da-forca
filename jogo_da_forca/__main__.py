# imports internos
from jogo_da_forca.objects import Hangman, Jogo, Menu
from jogo_da_forca.utils.terminal import cls, pause, finalizar_programa
from jogo_da_forca.utils.logger import informar, alertar, confirmar
from jogo_da_forca.utils.user_input import ler_opcao

# imports externos


def iniciar_partida():
    cls()
    hangman: Hangman = Hangman()
    jogo: Jogo = Jogo(hangman)
    while True:
        cls()
        jogo.exibir_status()
        jogo.turno()
        pause()
        finalizado, resultado, mensagem = jogo.checar_finalizacao()
        match finalizado:
            case True:
                match resultado:
                    case 'vitoria':
                        confirmar(mensagem)
                    case 'derrota':
                        informar(mensagem)
                pause()
                break
            case False:
                continue


def main():
    menu: Menu = Menu()
    cls()
    menu.exibir_regras()
    pause()
    try:
        while True:
            cls()
            menu.exibir_menu()
            opcao: str = ler_opcao("Escolha uma opção (1-3):\n> ", ["1", "2", "3"])
            match opcao:
                case '1':
                    iniciar_partida()
                case '2':
                    cls()
                    menu.exibir_regras()
                    pause()
                case '3':
                    finalizar_programa()
    except KeyboardInterrupt:
        finalizar_programa()

if __name__ == "__main__":
    main()
