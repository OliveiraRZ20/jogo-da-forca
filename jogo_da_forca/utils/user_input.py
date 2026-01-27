# imports internos
from jogo_da_forca.utils.logger import alertar, informar, confirmar
from jogo_da_forca.utils.validator import validar_tentativa

# imports externos


def ler_opcao(input_message: str, opcoes_validas: list[str]) -> str:
    """Função genérica para leitura de uma opção dentre as opções válidas fornecidas"""
    while True:
        opcao: str = input(input_message).strip()
        if opcao not in opcoes_validas:
            alertar("Opção inválida! Tente novamente.")
        else:
            return opcao


def ler_tentativa(input_message: str) -> str:
    """Função para leitura da tentativa do usuário durante o turno"""
    while True:
        tentativa: str = input(input_message).strip().lower()
        resultado, mensagem = validar_tentativa(tentativa)
        match resultado:
            case True:
                return tentativa
            case False:
                alertar(mensagem)
