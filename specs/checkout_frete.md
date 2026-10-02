# Especificação — Cálculo de Frete

## REQ-01 — Frete padrão

O sistema deverá cobrar uma taxa de frete de R$ 15,00 quando o subtotal do carrinho for inferior a R$ 250,00, desde que o subtotal seja válido.

## REQ-02 — Frete grátis

SE o subtotal do carrinho for maior ou igual a R$ 250,00, ENTÃO o sistema deverá conceder frete grátis, com taxa de R$ 0,00.

## REQ-03 — Valor mínimo válido

O sistema deverá rejeitar subtotais menores ou iguais a zero, lançando `ValueError`.

## REQ-04 — Valor numérico

O sistema deverá aceitar somente valores numéricos reais para o subtotal. Valores textuais, booleanos e outros tipos incompatíveis deverão ser rejeitados.

## REQ-05 — Limite de frete grátis

O sistema deverá aplicar frete grátis exatamente a partir de R$ 250,00, inclusive.

## REQ-06 — Valores decimais

O sistema deverá aceitar valores monetários com duas casas decimais, como R$ 99,90 e R$ 249,99.

## REQ-07 — Subtotal abaixo do limite

Para qualquer subtotal válido maior que zero e inferior a R$ 250,00, o sistema deverá retornar R$ 15,00 de frete.

## REQ-08 — Consistência

O resultado do cálculo deverá ser determinístico: entradas válidas iguais deverão produzir o mesmo valor de frete.

## REQ-09 — Ausência de cobrança duplicada

A função de cálculo deverá retornar apenas o valor do frete, sem adicionar o frete ao subtotal do carrinho.

## REQ-10 — Escopo limitado

O sistema não deverá aplicar cupons, descontos, taxas regionais ou regras de peso enquanto essas funcionalidades não forem especificadas formalmente.
