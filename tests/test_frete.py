
import pytest
from src.frete import calcular_frete


def test_frete_padrao():
    assert calcular_frete(100.00) == 15.00


def test_frete_gratis_no_limite():
    assert calcular_frete(250.00) == 0.00


def test_frete_gratis_acima_do_limite():
    assert calcular_frete(300.00) == 0.00


def test_frete_abaixo_do_limite():
    assert calcular_frete(249.99) == 15.00


def test_valor_decimal():
    assert calcular_frete(99.90) == 15.00


@pytest.mark.parametrize("subtotal", [0, -1, -100.00])
def test_rejeita_subtotal_invalido(subtotal):
    with pytest.raises(ValueError):
        calcular_frete(subtotal)


@pytest.mark.parametrize("subtotal", ["100", True, None])
def test_rejeita_tipo_incompativel(subtotal):
    with pytest.raises((ValueError, TypeError)):
        calcular_frete(subtotal)


def test_retorna_apenas_frete():
    # O subtotal é R$ 100,00, mas a função retorna somente o frete.
    assert calcular_frete(100.00) == 15.00


def test_resultado_deterministico():
    assert calcular_frete(150.00) == calcular_frete(150.00)