
def calcular_frete(subtotal, regiao):
    if subtotal < 0:
        raise ValueError("O subtotal não pode ser negativo.")

    if not isinstance(subtotal, (int, float)) or isinstance(subtotal, bool):
        raise ValueError("O subtotal deve ser numérico.")

    if subtotal > 300:
        return 0.00

    frete_base = 15.00

    if regiao in ("Norte", "Nordeste"):
        frete_base += 10.00

    return frete_base
