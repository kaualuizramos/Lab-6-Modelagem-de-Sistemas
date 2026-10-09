import pytest
from src.frete import calcular_frete

def calcular_frete_com_desconto_fidelidade(valor_carrinho, clube_fidelidade=False):
    """Nova funcionalidade simulada (6.5): Aplicação de desconto extra se for membro."""
    frete_base = calcular_frete(valor_carrinho)
    if clube_fidelidade and frete_base > 0:
        return 0.00 # Membros fidelidade ganham frete grátis independentemente
    return frete_base

def test_regressao_regras_originais_frete():
    """Garante que o comportamento padrão do frete permanece inalterado (Regressão)."""
    assert calcular_frete(100.00) == 15.00
    assert calcular_frete(250.00) == 0.00

def test_nova_funcionalidade_fidelidade():
    """Valida a nova funcionalidade de desconto por fidelidade sem afetar o comportamento base."""
    # Cliente sem fidelidade mantém a regra antiga
    assert calcular_frete_com_desconto_fidelidade(100.00, False) == 15.00
    
    # Cliente com fidelidade ganha o benefício na nova funcionalidade
    assert calcular_frete_com_desconto_fidelidade(100.00, True) == 0.00