
from unittest.mock import Mock
from src.frete import calcular_frete


def test_frete_com_test_doubles():
    # Arrange
    # Dummy: objeto fictício passado como sessão, sem uso na lógica.
    sessao_dummy = object()
    pedido_id = 123
    subtotal = 100.00
    taxa_fixa = 12.50

    # Stub: simula a API de logística, sem chamadas de rede.
    servico_logistica = Mock()
    servico_logistica.consultar_taxa.return_value = taxa_fixa

    # Mock/Spy: registra as chamadas de notificação.
    servico_notificacao = Mock()

    # Act
    taxa_consultada = servico_logistica.consultar_taxa(
        subtotal=subtotal
    )
    frete_calculado = calcular_frete(subtotal)

    # Considere o frete confirmado após a consulta e o cálculo.
    frete_confirmado = taxa_consultada
    if frete_confirmado >= 0:
        servico_notificacao.enviar_notificacao_rastreio(pedido_id)

    # Assert
    assert taxa_consultada == taxa_fixa
    assert frete_calculado == 15.00
    servico_logistica.consultar_taxa.assert_called_once_with(
        subtotal=subtotal
    )
    servico_notificacao.enviar_notificacao_rastreio.assert_called_once_with(
        pedido_id
    )
