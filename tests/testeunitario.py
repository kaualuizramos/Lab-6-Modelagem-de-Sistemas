import pytest
from src.conta import ContaBancaria, SaldoInsuficienteException

def test_unidade_deposito_valido():
    conta = ContaBancaria("101", 100.0)
    conta.depositar(50.0)
    assert conta.saldo == 150.0

def test_unidade_deposito_invalido():
    conta = ContaBancaria("101", 100.0)
    with pytest.raises(ValueError):
        conta.depositar(-10.0)

def test_unidade_saque_com_sucesso():
    conta = ContaBancaria("101", 200.0)
    conta.sacar(50.0)
    assert conta.saldo == 150.0

def test_unidade_saque_saldo_insuficiente():
    conta = ContaBancaria("101", 100.0)
    with pytest.raises(SaldoInsuficienteException):
        conta.sacar(150.0)
    assert conta.saldo == 100.0