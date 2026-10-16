
import pytest
from src.frete import calcular_frete


def test_frete_padrao():
    # Arrange
    subtotal = 100.00
    frete_esperado = 15.00

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


def test_frete_gratis_no_limite():
    # Arrange
    subtotal = 250.00
    frete_esperado = 0.00

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


def test_frete_gratis_acima_do_limite():
    # Arrange
    subtotal = 300.00
    frete_esperado = 0.00

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


def test_frete_abaixo_do_limite():
    # Arrange
    subtotal = 249.99
    frete_esperado = 15.00

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


def test_valor_decimal():
    # Arrange
    subtotal = 99.90
    frete_esperado = 15.00

    # Act
    frete = calcular_frete(subtotal)

    # Assert
    assert frete == frete_esperado


@pytest.mark.parametrize("subtotal", [0, -1, -100.00])
def test_rejeita_subtotal_invalido(subtotal):
    # Arrange
    valor = subtotal

    # Act
    # Assert
    with pytest.raises(ValueError):
        calcular_frete(valor)


@pytest.mark.parametrize("subtotal", ["100", True, None])
def test_rejeita_tipo_incompativel(subtotal):
    # Arrange
    valor = subtotal

    # Act
    # Assert
    with pytest.raises((ValueError, TypeError)):
        calcular_frete(valor)


def test_retorna_apenas_frete():
    # Arrange
    subtotal = 100.00
    frete_esperado = 15.00

    # Act
    resultado = calcular_frete(subtotal)

    # Assert
    assert resultado == frete_esperado


def test_resultado_deterministico():
    # Arrange
    subtotal = 150.00

    # Act
    primeiro_resultado = calcular_frete(subtotal)
    segundo_resultado = calcular_frete(subtotal)

    # Assert
    assert primeiro_resultado == segundo_resultado
