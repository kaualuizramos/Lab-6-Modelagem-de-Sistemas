import pytest
from src.frete import calcular_frete

def jornada_checkout_usuario(valor_carrinho):
    """Simula o fluxo completo de uma cotação de ponta a ponta no sistema."""
    frete = calcular_frete(valor_carrinho)
    total_geral = valor_carrinho + frete
    
    # Regra de negócio final da jornada
    elegivel_frete_gratis = (valor_carrinho >= 250.00)
    
    return {
        "total_carrinho": valor_carrinho,
        "frete": frete,
        "total_geral": total_geral,
        "frete_gratis": elegivel_frete_gratis
    }

def test_jornada_funcional_carrinho_abaixo_limite():
    """Simula a jornada de um utilizador com carrinho abaixo de R$ 250,00."""
    res = jornada_checkout_usuario(100.00)
    assert res["frete"] == 15.00
    assert res["total_geral"] == 115.00
    assert res["frete_gratis"] is False

def test_jornada_funcional_carrinho_acima_limite():
    """Simula a jornada de um utilizador com carrinho elegível a frete grátis."""
    res = jornada_checkout_usuario(300.00)
    assert res["frete"] == 0.00
    assert res["total_geral"] == 300.00
    assert res["frete_gratis"] is True