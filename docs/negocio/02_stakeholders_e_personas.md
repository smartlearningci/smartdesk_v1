# 2. Stakeholders e Personas

## 2.1. Stakeholders

Os principais intervenientes do SmartDesk são os colaboradores da NexaServ, os técnicos de suporte e a responsável de TI.

Para compreender as suas necessidades, foram definidas três personas representativas dos perfis de utilização.

Todos os utilizadores acedem com email e palavra-passe próprios do SmartDesk.

## 2.2. Persona 1 — Ana Martins

**Idade:** 32 anos  
**Função:** Assistente administrativa  
**Perfil:** Colaborador

**Contexto de trabalho:**  
A Ana trabalha no departamento administrativo da NexaServ e utiliza diariamente equipamentos e aplicações informáticas. Quando surge um problema, contacta a equipa de TI.

**Objetivo:**  
Comunicar problemas informáticos de forma simples e acompanhar a sua resolução.

**Dificuldades atuais:**
1. Não sabe se o seu pedido foi recebido ou registado.
2. Tem dificuldade em saber quando o problema ficará resolvido.

**Necessidades na aplicação:**
1. Iniciar e terminar sessão com as suas credenciais.
2. Criar tickets com uma descrição do problema e respetiva categoria.
3. Consultar exclusivamente o estado dos seus tickets.
4. Consultar a informação de resolução dos pedidos.

## 2.3. Persona 2 — Miguel Costa

**Idade:** 29 anos  
**Função:** Técnico de suporte  
**Perfil:** Técnico de suporte

**Contexto de trabalho:**  
O Miguel integra a equipa de TI da NexaServ. Recebe pedidos de diferentes departamentos e presta apoio na resolução de problemas de equipamento, software e acessos.

**Objetivo:**  
Organizar os pedidos que lhe são atribuídos e acompanhar o trabalho até à resolução.

**Dificuldades atuais:**
1. Os pedidos chegam por diferentes canais e nem sempre estão organizados.
2. Nem sempre é claro quais os pedidos que estão sob a sua responsabilidade.

**Necessidades na aplicação:**
1. Iniciar e terminar sessão.
2. Consultar os tickets atualmente atribuídos.
3. Atualizar o estado dos tickets durante o tratamento.
4. Registar a resolução e retomar tickets Resolvidos quando necessário.
5. Deixar de poder tratar tickets reatribuídos a outro técnico.

## 2.4. Persona 3 — Sofia Almeida

**Idade:** 43 anos  
**Função:** Responsável de TI  
**Perfil:** Responsável de TI

**Contexto de trabalho:**  
A Sofia coordena os três técnicos da equipa de TI da NexaServ e acompanha os pedidos de suporte dos diferentes departamentos.

**Objetivo:**  
Garantir a organização dos pedidos, a distribuição do trabalho e o acompanhamento da sua resolução.

**Dificuldades atuais:**
1. Não dispõe de uma visão centralizada dos pedidos existentes.
2. Tem dificuldade em acompanhar a distribuição e o progresso do trabalho dos técnicos.

**Necessidades na aplicação:**
1. Iniciar e terminar sessão.
2. Consultar todos os tickets e respetivos estados.
3. Atribuir e reatribuir tickets ainda não fechados aos técnicos de suporte.
4. Acompanhar os tickets por técnico e por estado.
5. Consultar históricos de estados e técnicos.
6. Fechar tickets Resolvidos.

## 2.5. Relação entre personas e funcionalidades

| Persona | Perfil | Funcionalidades necessárias |
|---|---|---|
| Ana Martins | Colaborador | Autenticar-se; criar tickets; consultar exclusivamente os próprios tickets, estados e resoluções. |
| Miguel Costa | Técnico de suporte | Autenticar-se; consultar tickets atualmente atribuídos; iniciar, retomar e resolver tratamento. |
| Sofia Almeida | Responsável de TI | Autenticar-se; consultar todos os tickets; atribuir e reatribuir; consultar históricos; fechar tickets Resolvidos. |

## 2.6. Regras comuns

- Cada utilizador tem credenciais próprias e um perfil associado.
- Apenas utilizadores autenticados acedem às funcionalidades internas.
- O Colaborador consulta apenas os seus pedidos.
- O Técnico trata apenas tickets atualmente atribuídos.
- Apenas a Responsável de TI atribui, reatribui e fecha tickets.
- Reatribuir não altera o estado; tickets Fechados não podem ser reatribuídos ou reabertos.
