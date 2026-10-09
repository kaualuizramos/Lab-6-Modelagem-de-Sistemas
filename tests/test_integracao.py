import pytest
from src.frete import calcular_frete

def simular_historico_cotacoes(valor_carrinho):
    """Componente auxiliar simulado para registrar a operação de frete."""
    frete = calcular_frete(valor_carrinho)
    registro = {
        "subtotal": valor_carrinho,
        "frete_aplicado": frete,
        "status": "sucesso"
    }
    return registro

def test_integracao_frete_com_historico():
    """Valida se o módulo de frete se integra corretamente com o registo de histórico."""
    carrinho = 200.00
    resultado = simular_historico_cotacoes(carrinho)
    
    assert resultado["subtotal"] == 200.00
    assert resultado["frete_aplicado"] == 15.00
    assert resultado["status"] == "sucesso"