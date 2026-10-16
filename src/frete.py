import math


def calcular_frete(valor_carrinho, regiao):
    # REQ-04: aceitar somente valores numéricos,
    # excluindo booleanos.
    if isinstance(valor_carrinho, bool) or not isinstance(
        valor_carrinho, (int, float)
    ):
        raise TypeError("O subtotal deve ser numérico.")

    # Rejeitar NaN e infinito.
    if not math.isfinite(valor_carrinho):
        raise ValueError("O subtotal deve ser um valor finito.")

    # REQ-03: subtotal deve ser maior que zero.
    if valor_carrinho <= 0:
        raise ValueError("O subtotal deve ser maior que zero.")

    # TDD: frete grátis somente acima de R$ 300,00.
    if valor_carrinho > 300.00:
        return 0.00

    # REQ-01: frete base.
    frete = 15.00

    # REQ-7.4: adicional para Norte e Nordeste.
    if regiao in ("Norte", "Nordeste"):
        frete += 10.00

    return frete