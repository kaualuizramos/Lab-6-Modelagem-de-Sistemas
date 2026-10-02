
from math import isfinite


def calcular_frete(valor_carrinho: float) -> float:
    if isinstance(valor_carrinho, bool):
        raise ValueError("Valor de carrinho inválido")

    if not isinstance(valor_carrinho, (int, float)):
        raise TypeError("O valor do carrinho deve ser numérico")

    if not isfinite(valor_carrinho) or valor_carrinho <= 0:
        raise ValueError("Valor de carrinho inválido")

    if valor_carrinho >= 250.00:
        return 0.00

    return 15.00