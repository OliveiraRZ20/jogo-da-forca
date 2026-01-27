# imports internos

# imports externos
from string import ascii_lowercase

def validar_tentativa(entry: str) -> tuple[bool, str]:
    """Valida a tentativa do usuário"""
    if entry == '':
        return [False, "Entrada inválida! Nenhum valor foi inserido."]
    elif any(char not in ascii_lowercase for char in entry):
        return [False, "Entrada inválida! Apenas letras são permitidas."]
    else:
        return [True, ""]
