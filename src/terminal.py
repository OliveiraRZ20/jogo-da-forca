from os import system

def cls() -> None:
    """Limpa o terminal do windows"""
    system("cls")
    return

def pause() -> None:
    """Pausa à execução do programa no terminal do windows"""
    system("pause")
    return

def mensagem_colorida(nome_cor: str, msg: str):
    """Retorna uma mensagem colorida para o terminal (Windows)"""
    dict_codigo_cor: dict[str, int] = {'vermelho': 31, 'verde': 32, 'amarelo': 33}
    return f"\033[{dict_codigo_cor[nome_cor]}m{msg}\033[0m"

def alertar(msg: str):
    """Exibe uma mensagem de alerta em vermelho"""
    print(mensagem_colorida('vermelho', f"[ERRO] {msg}"))

def informar(msg: str):
    """Exibe uma mensagem informativa em amarelo"""
    print(mensagem_colorida('amarelo', f"[INFO] {msg}"))

def confirmar(msg: str):
    """Exibe uma mensagem de confirmação em verde"""
    print(mensagem_colorida('verde', f"[SUCESSO] {msg}"))