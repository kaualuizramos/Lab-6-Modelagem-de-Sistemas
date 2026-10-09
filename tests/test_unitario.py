import pytest
import math
from src.frete import calcular_frete

def test_frete_gratis_acima_ou_igual_250():
    assert calcular_frete(250.00) == 0.00
    assert calcular_frete(300.0) == 0.00

def test_frete_padrao_abaixo_de_250():
    assert calcular_frete(100.0) == 15.00
    assert calcular_frete(10.50) == 15.00

def test_subtotal_invalido_tipo_booleano():
    with pytest.raises(TypeError):
        calcular_frete(True)
    with pytest.raises(TypeError):
        calcular_frete(False)

def test_subtotal_invalido_tipo_nao_numerico():
    with pytest.raises(TypeError):
        calcular_frete("250")

def test_subtotal_invalido_nao_finito():
    with pytest.raises(ValueError):
        calcular_frete(float('nan'))
    with pytest.raises(ValueError):
        calcular_frete(float('inf'))

def test_subtotal_menor_ou_igual_a_zero():
    with pytest.raises(ValueError):
        calcular_frete(0)
    with pytest.raises(ValueError):
        calcular_frete(-50.0)