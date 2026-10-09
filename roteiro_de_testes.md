## 1. Casos de Teste

### 1.1. Testes Unitários
* **ID:** `CT-UNIT-01`
* **Componente:** `Frete` (método de cálculo de peso/distância)
* **Entrada:** Peso do pacote = 0 kg ou negativo.
* **Resultado Esperado:** O sistema deve lançar uma exceção de valor inválido (`ValueError`) e recusar o cálculo.

### 1.2. Testes de Integração
* **ID:** `CT-INTEG-01`
* **Componente:** Integração entre a classe `Frete` e a classe de regras de cubagem/taxa de entrega.
* **Entrada:** Pacote com dimensões grandes que ultrapassam o limite de peso real, ativando o cálculo de peso cúbico integrado.
* **Resultado Esperado:** O sistema deve calcular corretamente o valor final utilizando o maior valor entre o peso real e o peso cúbico integrados.

### 1.3. Testes Funcionais
* **ID:** `CT-FUNC-01`
* **Componente:** Módulo completo de Cotação de Frete (End-to-End).
* **Entrada:** Inserção de CEP de origem, CEP de destino, dimensões, peso e seleção da modalidade (Expresso).
* **Resultado Esperado:** O sistema retorna o valor correto do frete e o prazo estimado de entrega formatados corretamente para o usuário.