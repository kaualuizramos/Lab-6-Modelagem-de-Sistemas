
import pytest
from src.frete import calcular_frete


@pytest.mark.parametrize(
    "regiao, subtotal, frete_esperado",
    [
        ("Norte", 100.00, 25.00),
        ("Nordeste", 100.00, 25.00),
        ("Sudeste", 100.00, 15.00),
        ("Sul", 100.00, 15.00),
        ("Centro-Oeste", 100.00, 15.00),
        ("Norte", 300.00, 25.00),
        ("Nordeste", 300.00, 25.00),
        ("Norte", 300.01, 0.00),
        ("Nordeste", 350.00, 0.00),
        ("Sudeste", 350.00, 0.00),
    ],
)
def test_regra_frete_por_regiao(regiao, subtotal, frete_esperado):
    # Arrange
    valor_carrinho = subtotal
    regiao_entrega = regiao

    # Act
    frete = calcular_frete(valor_carrinho, regiao_entrega)

    # Assert
    assert frete == frete_esperado
