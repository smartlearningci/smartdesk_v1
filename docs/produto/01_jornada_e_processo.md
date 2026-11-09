# Passo 3 — Jornada do utilizador e processo de tickets

**Objetivo:** Descrever o percurso de um pedido de suporte informático, desde a comunicação do problema até ao fecho do ticket.

## 1. Sequência narrativa — Problema de impressora

| Etapa | Responsável | Ação | Estado do ticket |
|---|---|---|---|
| 1 | **Ana Martins** | A impressora não funciona. Ana acede ao SmartDesk e cria um ticket na categoria Equipamento, descrevendo o problema. | Aberto |
| 2 | **Sofia Almeida** | Consulta os pedidos pendentes e atribui o ticket a Miguel, tendo em conta a distribuição do trabalho. | Aberto |
| 3 | **Miguel Costa** | Consulta o ticket atribuído e inicia a análise do problema. | Em tratamento |
| 4 | **Miguel Costa** | Verifica a impressora, identifica a causa e realiza a intervenção necessária. | Em tratamento |
| 5 | **Miguel Costa** | Regista a solução aplicada e assinala o ticket como resolvido. | Resolvido |
| 6 | **Ana Martins** | Pode consultar a resolução e comunicar se o problema persistir; não é exigida confirmação formal para o fecho. | Resolvido |
| 7 | **Sofia Almeida** | Verifica e confirma a resolução e fecha o ticket, sem exigir confirmação formal de Ana. | Fechado |

## 2. Principais decisões do processo

- **Quem trata o pedido?** Sofia atribui o ticket a um técnico e pode reatribuí-lo se necessário.
- **O problema foi resolvido?** Se não, Miguel continua o tratamento.
- **A resolução funcionou?** Se Ana indicar que o problema persiste, o ticket regressa de Resolvido a Em tratamento.
- **O ticket pode ser fechado?** Sofia verifica e confirma a resolução antes de o fechar, sem exigir confirmação formal de Ana.
- **Um ticket fechado pode ser reaberto?** Não. Um novo problema exige um novo ticket.

## 3. Fluxograma ASCII — Jornada do ticket

```text
ANA cria ticket — ABERTO
        |
        v
SOFIA atribui a Miguel — ABERTO
        |
        v
MIGUEL inicia tratamento — EM TRATAMENTO
        |
        v
  Problema resolvido?
      | NÃO                  SIM
      |                       |
      |                       v
      |             MIGUEL regista solução — RESOLVIDO
      |                       |
      |                       v
      |               Resolução mantém-se?
      |                 | NÃO         SIM
      |                 |             |
      |       ANA comunica problema   SOFIA verifica e confirma
      |                 |             |
      |                 v             v
      +-------> EM TRATAMENTO     SOFIA fecha — FECHADO
                       |
                       +----> MIGUEL retoma tratamento
```

Se o problema não estiver resolvido, mantém-se **Em tratamento**. Se Ana comunicar que persiste após a resolução, o ticket regressa a **Em tratamento**, mantendo o técnico responsável. Sofia pode reatribuir em **Aberto** ou **Em tratamento**, sem alterar automaticamente o estado. Só Sofia fecha após verificar a resolução, sem exigir confirmação formal de Ana. Um ticket **Fechado** não pode ser reaberto.

## 4. Resultado esperado

No final, o SmartDesk permite saber quem comunicou o problema, quem ficou responsável pelo tratamento, qual a solução aplicada e em que estado se encontra o pedido.
