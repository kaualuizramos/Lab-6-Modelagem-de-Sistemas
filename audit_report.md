# Relatório de Auditoria — Exercício 2

## 1. Objetivo
Verificar a rastreabilidade entre a especificação EARS,
os testes automatizados e o código implementado.

## 2. Matriz de Rastreabilidade

| Requisito | Teste correspondente | Implementação | Status |
|---|---|---|---|
| REQ-01: frete de R$ 15,00 abaixo de R$ 200,00 | test_cobrar_frete_abaixo_limite | src/frete.py — calcular_frete | Atendido |
| REQ-02: frete grátis a partir de R$ 200,00 | test_frete_gratis e test_frete_gratis_no_limite | src/frete.py — calcular_frete | Atendido |
| Validação de valor inválido | test_valor_carrinho_invalido | src/frete.py — validar valor | Atendido |

## 3. Drift e Sobre-implementação

O cupom DESCONTO10 não possui requisito correspondente
na especificação original.

Qualquer implementação desse cupom deve ser removida
enquanto não houver autorização formal na especificação.

Também devem ser removidos cupons adicionais, persistência
e logs extras que não sejam necessários aos requisitos.

## 4. Ação Corretiva

1. Remover o código de cupons não especificados.
2. Conferir o alinhamento entre código e especificação.
3. Executar novamente os testes Pytest.
4. Confirmar que todos os testes passam.
5. Revisar arquitetura, desempenho, segurança e observabilidade.

## 5. Conclusão

A implementação deve conter somente as funcionalidades
autorizadas pelos requisitos. Qualquer alteração de escopo
deve começar pela atualização da especificação.