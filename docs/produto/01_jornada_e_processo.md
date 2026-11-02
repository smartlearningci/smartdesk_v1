# 3. Jornada e Processo de um Ticket

## 3.1. Cenário

Ana Martins, assistente administrativa da NexaServ, precisa de imprimir um documento, mas a impressora não funciona.

Para comunicar o problema à equipa de TI, utiliza o SmartDesk.

Miguel Costa será o técnico responsável pela resolução e Sofia Almeida acompanhará a distribuição do trabalho.

## 3.2. Jornada do ticket

**1. Criação do pedido — Aberto**

- Ana acede ao SmartDesk no Chrome ou Edge e autentica-se com email e palavra-passe.
- O sistema reconhece o perfil Colaborador.
- Cria um ticket com o título "Impressora não funciona".
- Seleciona a categoria "Equipamento" e descreve o problema.
- Submete o pedido.

O SmartDesk regista o ticket com o estado **Aberto**.

**2. Atribuição do pedido — Aberto**

- Sofia consulta os tickets abertos.
- Verifica a distribuição do trabalho pelos técnicos.
- Atribui o ticket a Miguel Costa.
- Miguel autentica-se e consulta o novo ticket atribuído.

O ticket mantém-se no estado **Aberto** até Miguel iniciar o tratamento.

**3. Tratamento do pedido — Em tratamento**

- Miguel inicia a análise do problema.
- Atualiza o estado para **Em tratamento**.
- Verifica a impressora e procura identificar a causa.
- Ana pode consultar o estado do seu pedido.
- Se necessário, Sofia pode reatribuir o ticket a outro técnico, sem mudar o estado; o técnico anterior perde as permissões de tratamento e a alteração fica no histórico.
- Sofia acompanha o progresso do ticket.

**4. Resolução do problema — Resolvido**

- O técnico atualmente atribuído identifica e corrige o problema da impressora.
- Regista a solução aplicada.
- Altera o estado para **Resolvido**.
- Se a solução não for eficaz, o técnico atribuído pode retomar o estado **Em tratamento**.
- Ana consulta a informação de resolução.

**5. Encerramento do pedido — Fechado**

- Sofia consulta o ticket Resolvido e encerra o pedido.
- O ticket passa ao estado **Fechado**.
- O histórico do pedido permanece disponível para consulta.

Apenas Sofia pode fechar tickets Resolvidos. Um ticket Fechado não pode ser reaberto nem reatribuído. Cada utilizador pode terminar a sessão, preservando-se os dados.

## 3.3. Estados do ticket

| Estado | Significado |
|---|---|
| Aberto | Pedido registado e ainda não iniciado. |
| Em tratamento | Um técnico está a trabalhar na resolução. |
| Resolvido | O técnico registou a solução do problema. |
| Fechado | O pedido foi concluído e encerrado. |

## 3.4. Principais decisões do processo

**Decisão 0 — O utilizador está autenticado?**

- Não: não pode aceder às funcionalidades internas.
- Sim: pode executar apenas as operações autorizadas.

**Decisão 1 — O ticket já foi atribuído?**

- Não: aguarda atribuição pela responsável de TI.
- Sim: o técnico pode iniciar o tratamento.

**Decisão 2 — É necessário reatribuir o ticket?**

- Sim, e não está Fechado: Sofia pode alterar o técnico sem alterar o estado.
- Não: mantém-se o técnico atual.
- Se estiver Fechado: a reatribuição é rejeitada.

**Decisão 3 — O problema está resolvido?**

- Não: o ticket permanece Em tratamento.
- Sim: o técnico regista a solução e altera o estado para Resolvido.

**Decisão 4 — O ticket pode ser fechado?**

- Não: permanece Resolvido.
- Sim: passa ao estado Fechado.

Apenas a Responsável de TI executa o fecho.

## 3.5. Fluxograma do processo

```text
        ┌───────────────────────────┐
        │ Ana cria ticket           │
        │ Estado: ABERTO            │
        └─────────────┬─────────────┘
                      │
                      ▼
        ┌───────────────────────────┐
        │ Sofia atribui o ticket    │
        │ a Miguel                  │
        └─────────────┬─────────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Foi atribuído?  │
             └───────┬─────────┘
                     │
             Não ◄───┴───► Sim
              │             │
              ▼             ▼
       Aguarda         Miguel inicia
       atribuição      o tratamento
                            │
                            ▼
                    ┌────────────────┐
                    │ EM TRATAMENTO  │◄──────┐
                    └───────┬────────┘       │
                            │                │
                            ▼                │
                    ┌────────────────┐       │
                    │ Problema       │       │
                    │ resolvido?     │       │
                    └───────┬────────┘       │
                            │                │
                     Não ───┴────────────────┘
                            │ Sim
                            ▼
                    ┌────────────────┐
                    │ RESOLVIDO      │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ Pode fechar?   │
                    └───────┬────────┘
                            │
                     Não ───┤ (aguarda)
                            │ Sim
                            ▼
                    ┌────────────────┐
                    │ FECHADO        │
                    └────────────────┘
```

## 3.6. Regras consolidadas

1. O utilizador autentica-se antes de aceder às funcionalidades internas.
2. Existem apenas os três perfis aprovados.
3. Sofia atribui e reatribui tickets Aberto, Em tratamento ou Resolvido.
4. A reatribuição não altera o estado e fica registada no histórico.
5. Só o técnico atualmente atribuído pode iniciar, retomar ou resolver o tratamento.
6. Só Sofia fecha tickets Resolvidos.
7. Fechado é um estado terminal.
8. Os dados e históricos persistem após terminar a sessão.
