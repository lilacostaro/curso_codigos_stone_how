def calcula_media(lst: list) -> float:
    """Calcula a média aritmetica."""
    return sum(lst) / len(lst)

def calcula_media_ponderada(valores: list, pesos: list) -> float:
    """Calcula a média ponderada."""
    numerador = 0
    denominador = sum(pesos)
    for valor, peso in zip(valores, pesos):
        numerador = numerador + (valor * peso)
    return numerador / denominador