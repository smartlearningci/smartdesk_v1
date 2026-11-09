# language: pt

Funcionalidade: MVP SmartDesk
  Como utilizador da NexaServ
  Quero gerir pedidos de suporte informático
  Para acompanhar a sua resolução

  Cenário: US-001 - Autenticação
    Dado que Ana possui uma conta válida
    Quando introduz o email e a palavra-passe corretos
    Então consegue iniciar sessão
    E é identificada como colaboradora

  Cenário: US-002 - Criar ticket
    Dado que Ana iniciou sessão
    Quando cria um ticket com título e descrição
    E seleciona a categoria "Equipamento"
    Então o ticket é registado
    E fica no estado "Aberto"

  Cenário: US-003 - Consultar tickets
    Dado que Ana iniciou sessão
    E existem tickets de vários colaboradores
    Quando consulta os tickets
    Então visualiza apenas os seus pedidos
    E os respetivos estados

  Cenário: US-004 - Atribuir e reatribuir ticket
    Dado que Sofia iniciou sessão como responsável de TI
    E existe um ticket no estado "Aberto"
    Quando atribui o ticket a Miguel
    Então Miguel fica identificado como responsável
    Quando Sofia reatribui o ticket a outro técnico
    Então o novo técnico fica identificado como responsável
    E o estado do ticket mantém-se "Aberto"

  Cenário: US-005 - Consultar tickets atribuídos
    Dado que Miguel iniciou sessão como técnico
    E existem tickets atribuídos a Miguel
    Quando consulta a lista de tickets
    Então visualiza os tickets que lhe estão atribuídos

  Cenário: US-006 - Iniciar tratamento
    Dado que Miguel possui um ticket atribuído
    E o ticket está no estado "Aberto"
    Quando inicia o tratamento
    Então o estado passa a "Em tratamento"

  Cenário: US-007 - Registar resolução
    Dado que Miguel está a tratar um ticket
    E o ticket está no estado "Em tratamento"
    Quando regista a solução aplicada
    E assinala o ticket como resolvido
    Então o estado passa a "Resolvido"
    E a solução fica registada

  Cenário: US-008 - Regressar ao tratamento
    Dado que Ana possui um ticket no estado "Resolvido"
    E o ticket está atribuído a Miguel
    Quando comunica que o problema persiste
    Então o estado regressa a "Em tratamento"
    E Miguel mantém-se como responsável

  Cenário: US-009 - Acompanhar e fechar ticket
    Dado que Sofia iniciou sessão como responsável de TI
    E existe um ticket no estado "Resolvido"
    Quando consulta a solução registada
    E confirma a resolução sem exigir confirmação formal de Ana
    E fecha o ticket
    Então o estado passa a "Fechado"

  Cenário: US-010 - Validar campos obrigatórios
    Dado que Ana iniciou sessão
    Quando tenta criar um ticket sem um dos campos obrigatórios título, descrição ou categoria
    Então o ticket não é criado
    E o campo em falta é identificado
    E é apresentada uma mensagem clara

  Cenário: US-011 - Verificar desempenho
    Dado que Miguel iniciou sessão
    E estão documentadas as condições de medição no ambiente local de demonstração
    Quando acede às páginas principais de autenticação, criação e consulta de tickets
    Então cada página responde em até 3 segundos

  Esquema do Cenário: US-012 - Compatibilidade
    Dado que Ana utiliza o navegador "<navegador>"
    E possui uma conta válida
    Quando inicia sessão
    E cria um ticket com os campos obrigatórios
    Então consegue registar o ticket
    E visualiza o estado "Aberto"

    Exemplos:
      | navegador |
      | Chrome    |
      | Edge      |
