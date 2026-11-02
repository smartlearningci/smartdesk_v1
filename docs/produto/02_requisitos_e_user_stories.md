# 4. Requisitos e User Stories do SmartDesk

## 4.1. Objetivo

O SmartDesk é uma aplicação web interna destinada a centralizar e acompanhar os pedidos de suporte informático da NexaServ.

A primeira versão permitirá registar, atribuir, tratar, resolver e fechar tickets, substituindo a gestão dispersa por email, telefone, mensagens e folhas de cálculo.

Este documento define os requisitos, os perfis de utilização, as regras de funcionamento, as User Stories e a rastreabilidade dos cenários de aceitação.

## 4.2. Perfis de utilizador e permissões

Um **perfil** é um conjunto de permissões que determina as operações que um utilizador pode executar na aplicação.

O SmartDesk terá exatamente três perfis:

| Perfil | Persona | Permissões |
|---|---|---|
| Colaborador | Ana Martins | Criar tickets; consultar os próprios tickets, estados e resoluções. |
| Técnico de suporte | Miguel Costa | Consultar os tickets atribuídos; iniciar e retomar o tratamento; registar resoluções. |
| Responsável de TI | Sofia Almeida | Consultar todos os tickets; atribuir tickets aos técnicos; acompanhar os estados; fechar tickets resolvidos; consultar históricos. |

Cada utilizador terá um perfil associado.

As permissões devem ser verificadas em cada operação. Um utilizador não pode consultar ou modificar informações fora das permissões do seu perfil.

## 4.3. Requisitos funcionais

Os requisitos funcionais descrevem aquilo que o sistema deve permitir fazer.

| ID | Requisito |
|---|---|
| RF-001 | Permitir o acesso de utilizadores identificados, associados a um dos três perfis: Colaborador, Técnico de suporte ou Responsável de TI. |
| RF-002 | Permitir ao Colaborador criar tickets e consultar exclusivamente os seus próprios pedidos. |
| RF-003 | Permitir ao Técnico de suporte consultar e tratar exclusivamente os tickets que lhe foram atribuídos. |
| RF-004 | Permitir à Responsável de TI consultar todos os tickets, atribuí-los aos técnicos e acompanhar a sua evolução. |
| RF-005 | Registar cada ticket com identificador único, título, descrição, categoria, autor, data de criação e estado. Título, descrição e categoria são campos obrigatórios. |
| RF-006 | Disponibilizar exclusivamente as categorias Equipamento, Software e Acessos. |
| RF-007 | Criar automaticamente todos os tickets no estado Aberto. |
| RF-008 | Permitir à Responsável de TI atribuir tickets aos técnicos, sem alterar automaticamente o estado. |
| RF-009 | Permitir exclusivamente ao técnico atribuído alterar o estado de Aberto para Em tratamento. |
| RF-010 | Permitir exclusivamente ao técnico atribuído registar uma solução e alterar o estado de Em tratamento para Resolvido. O registo da solução é obrigatório. |
| RF-011 | Permitir ao técnico atribuído alterar um ticket de Resolvido para Em tratamento, quando o problema persistir. |
| RF-012 | Permitir exclusivamente à Responsável de TI alterar um ticket de Resolvido para Fechado. |
| RF-013 | Impedir transições de estado não autorizadas. Um ticket Fechado não pode voltar a qualquer outro estado. |
| RF-014 | Permitir ao Colaborador consultar o estado e a informação de resolução dos seus tickets. |
| RF-015 | Guardar o histórico das alterações de estado, incluindo data, utilizador e transição efetuada. |
| RF-016 | Permitir à Responsável de TI consultar os tickets por técnico atribuído e por estado. |

## 4.4. Requisitos não funcionais

Os requisitos não funcionais descrevem as condições de qualidade e funcionamento do sistema.

| ID | Requisito |
|---|---|
| RNF-001 | A aplicação deve funcionar num navegador web suportado, sem instalação de software adicional. |
| RNF-002 | A interface deve ser simples, clara e compreensível para utilizadores sem conhecimentos técnicos. |
| RNF-003 | As permissões devem ser verificadas em cada operação, impedindo acessos e alterações não autorizados. |
| RNF-004 | Os tickets, as resoluções e os históricos devem permanecer guardados após terminar a sessão. |
| RNF-005 | A aplicação deve apresentar mensagens claras quando uma operação não é permitida ou não pode ser concluída. |

Antes da execução dos testes, será necessário identificar os navegadores suportados e definir critérios objetivos para avaliar a facilidade de utilização.

## 4.5. Categorias e estados

### Categorias

Cada ticket pertence obrigatoriamente a uma das três categorias:

- **Equipamento:** problemas relacionados com computadores, impressoras ou outros equipamentos.
- **Software:** problemas relacionados com aplicações e programas.
- **Acessos:** problemas relacionados com permissões e acesso a sistemas.

Não existe a categoria Outros na primeira versão.

### Estados

| Estado | Significado |
|---|---|
| Aberto | Pedido registado, cujo tratamento ainda não foi iniciado. |
| Em tratamento | O técnico atribuído está a trabalhar na resolução. |
| Resolvido | O técnico registou uma solução para o problema. |
| Fechado | Pedido encerrado definitivamente pela Responsável de TI. |

## 4.6. Regras de transição entre estados

### Transições permitidas

| Estado de origem | Estado de destino | Utilizador autorizado | Condição |
|---|---|---|---|
| Aberto | Em tratamento | Técnico atribuído | Início do tratamento. |
| Em tratamento | Resolvido | Técnico atribuído | Registo obrigatório da solução. |
| Resolvido | Em tratamento | Técnico atribuído | Necessidade de retomar o tratamento. |
| Resolvido | Fechado | Responsável de TI | Encerramento do pedido. |

Todas as outras transições são proibidas.

### Diagrama de estados

```text
                 ┌──────────────────┐
                 │      ABERTO      │
                 └────────┬─────────┘
                          │
                          │ Técnico inicia tratamento
                          ▼
                 ┌──────────────────┐
          ┌─────►│  EM TRATAMENTO   │
          │      └────────┬─────────┘
          │               │
          │               │ Técnico regista solução
          │               ▼
          │      ┌──────────────────┐
          └──────┤    RESOLVIDO     │
                 └────────┬─────────┘
                          │
                          │ Responsável de TI fecha
                          ▼
                 ┌──────────────────┐
                 │     FECHADO      │
                 └──────────────────┘
                     ESTADO FINAL
```

A seta de retorno de Resolvido para Em tratamento representa a possibilidade de o técnico retomar o trabalho quando a solução não foi eficaz.

### Regras adicionais

1. Todos os tickets começam no estado Aberto.
2. A atribuição de um técnico não altera automaticamente o estado.
3. Apenas o técnico atribuído pode iniciar o tratamento, registar a resolução ou retomar o trabalho.
4. Não é possível resolver um ticket sem registar uma solução.
5. Não é possível passar diretamente de Aberto para Resolvido ou Fechado.
6. Não é possível passar diretamente de Em tratamento para Fechado.
7. Apenas a Responsável de TI pode fechar tickets.
8. Um ticket Fechado não pode ser reaberto nem mudar de estado, independentemente do perfil do utilizador.
9. As alterações de estado devem ficar registadas no histórico.

## 4.7. User Stories

As User Stories descrevem necessidades dos utilizadores, no formato:

"Como [persona], quero [ação], para [benefício]."

| ID | User Story | Requisitos associados |
|---|---|---|
| US-001 | Como Ana Martins, quero criar um ticket, para comunicar um problema informático. | RF-002, RF-005, RF-006, RF-007 |
| US-002 | Como Ana Martins, quero consultar os meus tickets, para acompanhar os pedidos e as respetivas resoluções. | RF-002, RF-014 |
| US-003 | Como Sofia Almeida, quero consultar todos os tickets, para acompanhar o trabalho da equipa. | RF-004, RF-016 |
| US-004 | Como Sofia Almeida, quero atribuir tickets aos técnicos, para organizar a distribuição do trabalho. | RF-008 |
| US-005 | Como Miguel Costa, quero consultar os tickets atribuídos, para saber quais os pedidos que devo tratar. | RF-003 |
| US-006 | Como Miguel Costa, quero iniciar o tratamento de um ticket, para indicar que estou a trabalhar no problema. | RF-009 |
| US-007 | Como Miguel Costa, quero registar a resolução de um ticket, para documentar a solução aplicada. | RF-010 |
| US-008 | Como Miguel Costa, quero retomar um ticket resolvido, para corrigir um problema que persiste. | RF-011 |
| US-009 | Como Sofia Almeida, quero fechar tickets resolvidos, para concluir formalmente os pedidos. | RF-012, RF-013 |
| US-010 | Como Sofia Almeida, quero consultar o histórico dos tickets, para acompanhar as alterações realizadas. | RF-015 |

O RF-001 e os requisitos não funcionais são transversais às histórias.

## 4.8. Critérios de aceitação

Cada User Story terá pelo menos um cenário de aceitação no formato Gherkin:

- **Dado:** situação inicial.
- **Quando:** ação executada.
- **Então:** resultado esperado.

Serão igualmente criados cenários para verificar regras de negócio, permissões, validação de dados, persistência e transições proibidas.

Os cenários encontram-se no ficheiro `features/tickets.feature`.

## 4.9. Matriz de rastreabilidade

A matriz relaciona os requisitos com os cenários Gherkin que os verificam.

### Requisitos funcionais

| Requisito | Cenários associados |
|---|---|
| RF-001 | US-001, RT-006 |
| RF-002 | US-001, US-002, RT-005 |
| RF-003 | US-005, US-006, US-007, RT-016 |
| RF-004 | US-003, US-004, US-009 |
| RF-005 | US-001, RT-017 |
| RF-006 | US-001, RT-007, RT-008 |
| RF-007 | US-001 |
| RF-008 | US-004 |
| RF-009 | US-006, RT-016 |
| RF-010 | US-007, RT-009 |
| RF-011 | US-008 |
| RF-012 | US-009, RT-003 |
| RF-013 | RT-001, RT-002, RT-003, RT-004, RT-010, RT-015, RT-018 |
| RF-014 | US-002 |
| RF-015 | US-006, US-008, US-010, RT-014 |
| RF-016 | US-003, RT-011 |

### Requisitos não funcionais

| Requisito | Cenários associados |
|---|---|
| RNF-001 | RT-012 |
| RNF-002 | RT-013 |
| RNF-003 | RT-003, RT-005, RT-006, RT-016, RT-018 |
| RNF-004 | RT-014 |
| RNF-005 | RT-008, RT-015, RT-016, RT-017 |

### Resumo de rastreabilidade

| Elemento | Quantidade |
|---|---:|
| Requisitos funcionais | 16 |
| Requisitos não funcionais | 5 |
| User Stories | 10 |
| Cenários principais | 10 |
| Cenários e esquemas adicionais | 18 |
| Total de cenários e esquemas | 28 |
| Requisitos associados a cenários | 21 de 21 |

A matriz demonstra a existência de cenários para todos os requisitos. A aprovação dos critérios não equivale à execução dos testes.

## 4.10. Limites do MVP

A primeira versão não incluirá:

- Aplicação móvel.
- Notificações por SMS.
- Integração com email.
- Resolução automática com Inteligência Artificial.
- Gestão complexa de SLA.

Não serão acrescentados perfis, categorias ou estados.

As validações, o histórico e as verificações de permissões não representam novos módulos funcionais: são necessários para garantir o funcionamento correto e verificável das funcionalidades já definidas.

## 4.11. Decisões pendentes

Antes da implementação, será necessário esclarecer:

1. Como serão identificados e autenticados os utilizadores.
2. Se a Responsável de TI poderá reatribuir tickets e em que condições.
3. Quais os navegadores web suportados.
4. Qual o critério mensurável de facilidade de utilização.

Estas decisões serão tratadas nas etapas adequadas, sem alterar as regras de negócio já aprovadas.
