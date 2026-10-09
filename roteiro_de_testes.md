## Casos de Teste

### 1. Testes Unitários
Os testes unitários validam o menor componente isolado do sistema, focando nas regras de negócio de classes individuais (como a classe `ContaBancaria`).

* **ID do Caso de Teste:** `CT-UNIT-01`
* **Módulo/Classe:** `ContaBancaria` (método `sacar`)
* **Descrição:** Validar o comportamento do sistema ao tentar realizar um saque com valor superior ao saldo disponível na conta.
* **Pré-condições:** 
  - A conta bancária deve estar criada.
  - Saldo atual da conta: R$ 100,00.
* **Dados de Entrada:** 
  - Valor do saque: R$ 150,00.
* **Resultado Esperado:** 
  - O sistema deve recusar a operação, lançando uma exceção de saldo insuficiente (`SaldoInsuficienteException` ou `ValueError`).
  - O saldo da conta deve permanecer inalterado em R$ 100,00.

---

### 2. Testes de Integração
Os testes de integração verificam a comunicação e o fluxo de dados correto entre dois ou mais módulos ou componentes do sistema integrados.

* **ID do Caso de Teste:** `CT-INTEG-01`
* **Módulo/Componente:** Integração entre `ContaBancaria` e `ServicoDeTransacao` (ou repositório de histórico).
* **Descrição:** Verificar se ao efetuar um depósito válido em uma conta, a transação é registrada corretamente na camada de histórico/extrato.
* **Pré-condições:** 
  - Conta bancária instanciada com saldo inicial de R$ 0,00.
  - Serviço de transações conectado à conta.
* **Dados de Entrada:** 
  - Operação de depósito no valor de R$ 200,00.
* **Resultado Esperado:** 
  - O saldo atualizado da conta deve ser de R$ 200,00.
  - Um registro de transação com os detalhes do depósito deve ser gravado e recuperável com sucesso na lista/banco de histórico da conta.

---

### 3. Testes Funcionais
Os testes funcionais (ou de sistema) avaliam o comportamento de ponta a ponta (End-to-End) simulando uma jornada real do usuário perante os requisitos do sistema.

* **ID do Caso de Teste:** `CT-FUNC-01`
* **Módulo/Componente:** Módulo de Transferência Bancária (Interface/Controlador principal).
* **Descrição:** Validar o fluxo completo de uma transferência de valores entre duas contas distintas sob a perspectiva do usuário final.
* **Pré-condições:** 
  - Conta de Origem (Conta A) com saldo de R$ 500,00.
  - Conta de Destino (Conta B) com saldo de R$ 100,00.
* **Dados de Entrada:** 
  - Conta Origem: `A`
  - Conta Destino: `B`
  - Valor da transferência: R$ 150,00.
* **Resultado Esperado:** 
  - O saldo da Conta Origem deve ser debitado para R$ 350,00.
  - O saldo da Conta Destino deve ser creditado para R$ 250,00.
  - O sistema deve gerar e exibir uma mensagem de sucesso na tela/terminal acompanhada do comprovante da transação.