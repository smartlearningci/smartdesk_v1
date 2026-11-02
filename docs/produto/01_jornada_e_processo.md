# 3. Jornada e Processo de um Ticket

## 3.1. Cenário

Ana Martins, assistente administrativa da NexaServ, precisa de imprimir um documento, mas a impressora não funciona.

Para comunicar o problema à equipa de TI, utiliza o SmartDesk.

Miguel Costa será o técnico responsável pela resolução e Sofia Almeida acompanhará a distribuição do trabalho.

## 3.2. Jornada do ticket

**1. Criação do pedido — Aberto**

- Ana acede ao SmartDesk.
- Cria um ticket com o título "Impressora não funciona".
- Seleciona a categoria "Equipamento" e descreve o problema.
- Submete o pedido.

O SmartDesk regista o ticket com o estado **Aberto**.

**2. Atribuição do pedido — Aberto**

- Sofia consulta os tickets abertos.
- Verifica a distribuição do trabalho pelos técnicos.
- Atribui o ticket a Miguel Costa.
- Miguel consulta o novo ticket atribuído.

O ticket mantém-se no estado **Aberto** até Miguel iniciar o tratamento.

**3. Tratamento do pedido — Em tratamento**

- Miguel inicia a análise do problema.
- Atualiza o estado para **Em tratamento**.
- Verifica a impressora e procura identificar a causa.
- Ana pode consultar o estado do seu pedido.
- Sofia acompanha o progresso do ticket.

**4. Resolução do problema — Resolvido**

- Miguel identifica e corrige o problema da impressora.
- Regista a solução aplicada.
- Altera o estado para **Resolvido**.
- Ana consulta a informação de resolução.

**5. Encerramento do pedido — Fechado**

- O problema é considerado concluído.
- O ticket passa ao estado **Fechado**.
- O histórico do pedido permanece disponível para consulta.

A responsabilidade pelo fecho será definida posteriormente.

## 3.3. Estados do ticket

| Estado | Significado |
|---|---|
| Aberto | Pedido registado e ainda não iniciado. |
| Em tratamento | Um técnico está a trabalhar na resolução. |
| Resolvido | O técnico registou a solução do problema. |
| Fechado | O pedido foi concluído e encerrado. |

## 3.4. Principais decisões do processo

**Decisão 1 — O ticket já foi atribuído?**

- Não: aguarda atribuição pela responsável de TI.
- Sim: o técnico pode iniciar o tratamento.

**Decisão 2 — O problema está resolvido?**

- Não: o ticket permanece Em tratamento.
- Sim: o técnico regista a solução e altera o estado para Resolvido.

**Decisão 3 — O ticket pode ser fechado?**

- Não: permanece Resolvido.
- Sim: passa ao estado Fechado.

Quem autoriza ou executa o fecho será definido nas próximas etapas.

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

## 3.6. Questões pendentes

1. Quem tem autorização para fechar um ticket?
2. É necessária confirmação da colaboradora antes do fecho?
3. Como deve ser tratado um ticket que permanece sem resolução?

Estas decisões serão esclarecidas posteriormente, sem alterar os quatro estados definidos para o SmartDesk.
