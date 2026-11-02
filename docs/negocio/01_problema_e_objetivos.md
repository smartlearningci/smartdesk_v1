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
- A alteração do técnico responsável nem sempre fica devidamente documentada.
- É difícil acompanhar o estado e a resolução dos problemas.
- A responsável de TI não dispõe de uma visão centralizada do trabalho da equipa.

## 1.3. Objetivos do projeto

O SmartDesk será uma aplicação web interna destinada a organizar os pedidos de suporte informático.

Os principais objetivos são:

1. Centralizar os pedidos numa única aplicação.
2. Permitir que os colaboradores registem e acompanhem os seus pedidos.
3. Facilitar a atribuição e reatribuição dos pedidos aos técnicos.
4. Acompanhar o estado de cada pedido até ao seu fecho.
5. Melhorar a organização e a visibilidade do trabalho da equipa de TI.
6. Garantir autenticação por email e palavra-passe e permissões por perfil.

## 1.4. Melhorias esperadas

Com o SmartDesk, espera-se:

- Reduzir a perda de pedidos.
- Tornar mais clara a responsabilidade por cada ticket.
- Facilitar a redistribuição do trabalho entre técnicos e registar as alterações.
- Facilitar o acompanhamento dos problemas.
- Melhorar a comunicação entre colaboradores e equipa de TI.
- Permitir à responsável de TI acompanhar os pedidos existentes.

## 1.5. Limites da primeira versão (MVP)

A primeira versão incluirá:

- Três perfis: Colaborador, Técnico de suporte e Responsável de TI.
- Autenticação por email e palavra-passe próprios do SmartDesk, início e fim de sessão.
- Atribuição e reatribuição de tickets não fechados, com histórico.
- Funcionamento no Google Chrome e Microsoft Edge.
- Categorias: Equipamento, Software e Acessos.
- Estados: Aberto, Em tratamento, Resolvido e Fechado.
- Percurso: criar, atribuir, tratar, resolver e fechar tickets.

**Ficam fora da primeira versão:**

- Aplicação móvel.
- Notificações por SMS.
- Resolução automática com Inteligência Artificial.
- Integração com email.
- Gestão complexa de prazos de atendimento (SLA).
- Recuperação automática de palavra-passe, autenticação multifator e integração com serviços externos de identidade.

## 1.6. Decisões tomadas

1. Apenas a Responsável de TI fecha tickets Resolvidos.
2. Apenas a Responsável de TI atribui ou reatribui tickets.
3. Título, descrição e categoria são obrigatórios.
4. Autenticação por email e palavra-passe próprios do SmartDesk.
5. Reatribuição permitida em Aberto, Em tratamento e Resolvido, mas não em Fechado.
6. Compatibilidade com Google Chrome e Microsoft Edge.

A classificação por prioridade dos pedidos não faz parte do MVP.
