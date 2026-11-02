# 1. Problema de Negócio e Objetivos

## 1.1. Contexto

A NexaServ é uma empresa fictícia de consultoria e serviços tecnológicos, com 60 colaboradores, distribuídos entre a sede e o trabalho remoto.

A equipa de TI é composta por três técnicos de suporte e uma responsável.

## 1.2. Problema de negócio

Atualmente, os colaboradores comunicam problemas informáticos por email, telefone ou mensagens.

A equipa de TI utiliza uma caixa de correio partilhada e uma folha de cálculo para organizar os pedidos.

Este processo apresenta várias dificuldades:

- Alguns pedidos perdem-se ou ficam sem resposta.
- Nem sempre é claro quem é responsável por cada pedido.
- É difícil acompanhar o estado e a resolução dos problemas.
- A responsável de TI não dispõe de uma visão centralizada do trabalho da equipa.

## 1.3. Objetivos do projeto

O SmartDesk será uma aplicação web interna destinada a organizar os pedidos de suporte informático.

Os principais objetivos são:

1. Centralizar os pedidos numa única aplicação.
2. Permitir que os colaboradores registem e acompanhem os seus pedidos.
3. Facilitar a atribuição dos pedidos aos técnicos.
4. Acompanhar o estado de cada pedido até ao seu fecho.
5. Melhorar a organização e a visibilidade do trabalho da equipa de TI.

## 1.4. Melhorias esperadas

Com o SmartDesk, espera-se:

- Reduzir a perda de pedidos.
- Tornar mais clara a responsabilidade por cada ticket.
- Facilitar o acompanhamento dos problemas.
- Melhorar a comunicação entre colaboradores e equipa de TI.
- Permitir à responsável de TI acompanhar os pedidos existentes.

## 1.5. Limites da primeira versão (MVP)

A primeira versão incluirá:

- Três perfis: Colaborador, Técnico de suporte e Responsável de TI.
- Categorias: Equipamento, Software e Acessos.
- Estados: Aberto, Em tratamento, Resolvido e Fechado.
- Percurso: criar, atribuir, tratar, resolver e fechar tickets.

**Ficam fora da primeira versão:**

- Aplicação móvel.
- Notificações por SMS.
- Resolução automática com Inteligência Artificial.
- Integração com email.
- Gestão complexa de prazos de atendimento (SLA).

## 1.6. Decisões pendentes

Antes da implementação, será necessário esclarecer:

1. Quem pode fechar um ticket?
2. Quem pode atribuir ou reatribuir tickets?
3. Que informações são obrigatórias na criação de um pedido?
4. Como será identificada a prioridade dos pedidos?

Estas decisões serão tratadas nas próximas etapas da especificação.
