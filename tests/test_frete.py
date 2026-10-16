
import pytest
from src.frete import calcular_frete


# Regra base de frete e limite de gratuidade.
@pytest.mark.parametrize(
    "subtotal, regiao, esperado",
    [
        (100.00, "Sudeste", 15.00),
        (249.99, "Sudeste", 15.00),
        (250.00, "Sudeste", 15.00),
        (300.00, "Sudeste", 15.00),
        (300.01, "Sudeste", 0.00),
        (500.00, "Sul", 0.00),
    ],
)
def test_frete_base_e_gratuidade(subtotal, regiao, esperado):
    # Arrange
    valor_carrinho = subtotal
    regiao_entrega = regiao

    # Act
    frete = calcular_frete(valor_carrinho, regiao_entrega)

    # Assert
    assert frete == esperado


# Nova regra de taxa regional.
@pytest.mark.parametrize(
    "regiao, subtotal, esperado",
    [
        ("Norte", 100.00, 25.00),
        ("Nordeste", 100.00, 25.00),
        ("Norte", 249.99, 25.00),
        ("Nordeste", 250.00, 25.00),
        ("Norte", 300.00, 25.00),
        ("Nordeste", 300.00, 25.00),
        ("Norte", 300.01, 0.00),
        ("Nordeste", 350.00, 0.00),
    ],
)
def test_regra_frete_por_regiao(regiao, subtotal, esperado):
    # Arrange
    valor_carrinho = subtotal
    regiao_entrega = regiao

    # Act
    frete = calcular_frete(valor_carrinho, regiao_entrega)

    # Assert
    assert frete == esperado


# Validação de valores inválidos.
@pytest.mark.parametrize("subtotal", [0, -1, -100.00])
def test_rejeita_subtotal_invalido(subtotal):
    # Arrange
    valor_carrinho = subtotal
    regiao = "Sudeste"

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_frete(valor_carrinho, regiao)


@pytest.mark.parametrize("subtotal", ["100", True, None])
def test_rejeita_tipo_incompativel(subtotal):
    # Arrange
    valor_carrinho = subtotal
    regiao = "Sudeste"

    # Act / Assert
    with pytest.raises(TypeError):
        calcular_frete(valor_carrinho, regiao)


@pytest.mark.parametrize("subtotal", [float("nan"), float("inf"), float("-inf")])
def test_rejeita_valores_nao_finitos(subtotal):
    # Arrange
    valor_carrinho = subtotal
    regiao = "Sudeste"

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_frete(valor_carrinho, regiao)


def test_valor_decimal():
    # Arrange
    subtotal = 99.90
    regiao = "Sudeste"

    # Act
    frete = calcular_frete(subtotal, regiao)

    # Assert
    assert frete == 15.00


def test_retorna_apenas_frete():
    # Arrange
    subtotal = 100.00
    regiao = "Norte"

    # Act
    resultado = calcular_frete(subtotal, regiao)

    # Assert
    assert resultado == 25.00


def test_resultado_deterministico():
    # Arrange
    subtotal = 150.00
    regiao = "Nordeste"

    # Act
    primeiro = calcular_frete(subtotal, regiao)
    segundo = calcular_frete(subtotal, regiao)

    # Assert
    assert primeiro == segundo
