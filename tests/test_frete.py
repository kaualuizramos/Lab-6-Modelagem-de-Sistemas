
import pytest
from src.frete import calcular_frete


def test_frete_gratis_acima_limite():
    assert calcular_frete(300.00) == 0.00


def test_frete_gratis_no_limite():
    assert calcular_frete(250.00) == 0.00


def test_frete_pago_abaixo_limite():
    assert calcular_frete(249.99) == 15.00


def test_frete_pago_valor_baixo():
    assert calcular_frete(50.00) == 15.00


def test_frete_pago_com_centavos():
    assert calcular_frete(99.90) == 15.00


@pytest.mark.parametrize("valor", [0, -1, -100.00])
def test_rejeita_valores_nao_positivos(valor):
    with pytest.raises(ValueError):
        calcular_frete(valor)


@pytest.mark.parametrize("valor", ["100", None, True, False, [], {}])
def test_rejeita_tipos_invalidos(valor):
    with pytest.raises((ValueError, TypeError)):
        calcular_frete(valor)


def test_retorna_apenas_o_frete():
    assert calcular_frete(100.00) == 15.00
    assert calcular_frete(300.00) == 0.00


def test_resultado_deterministico():
    assert calcular_frete(100.00) == calcular_frete(100.00)