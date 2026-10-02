
import math


def calcular_frete(valor_carrinho):
    # REQ-04: aceitar somente valores numéricos reais,
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

    # REQ-02 e REQ-05: frete grátis a partir de R$ 250,00.
    if valor_carrinho >= 250.00:
        return 0.00

    # REQ-01 e REQ-07: frete padrão abaixo do limite.
    return 15.00