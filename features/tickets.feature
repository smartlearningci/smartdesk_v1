# language: pt
Funcionalidade: Gestão de tickets SmartDesk
  Como utilizador da NexaServ
  Quero gerir pedidos de suporte informático
  Para acompanhar a sua resolução

  # ==========================================
  # CENÁRIOS DAS USER STORIES
  # ==========================================

  Cenário: US-001 - Criar um ticket
    Dado que Ana Martins acedeu ao SmartDesk como Colaborador
    Quando cria um ticket com título "Impressora não funciona"
    E preenche a descrição do problema
    E seleciona a categoria "Equipamento"
    E submete o pedido
    Então o sistema regista um ticket com identificador único
    E o estado inicial é "Aberto"
    E a data de criação e a autora ficam registadas

  Cenário: US-002 - Consultar os próprios tickets
    Dado que Ana Martins tem tickets registados
    Quando consulta os seus tickets
    Então visualiza os respetivos estados
    E visualiza a informação de resolução disponível
    E não visualiza tickets de outros colaboradores

  Cenário: US-003 - Consultar todos os tickets
    Dado que Sofia Almeida acedeu como Responsável de TI
    E existem tickets registados
    Quando consulta a lista de tickets
    Então visualiza todos os tickets
    E pode consultar os tickets por técnico e por estado

  Cenário: US-004 - Atribuir um ticket
    Dado que existe um ticket no estado "Aberto"
    E Sofia Almeida acedeu como Responsável de TI
    Quando atribui o ticket a Miguel Costa
    Então Miguel Costa fica responsável pelo ticket
    E o estado permanece "Aberto"

  Cenário: US-005 - Consultar tickets atribuídos
    Dado que Miguel Costa acedeu como Técnico de suporte
    E tem tickets atribuídos
    Quando consulta os tickets atribuídos
    Então visualiza os seus tickets e respetivos estados

  Cenário: US-006 - Iniciar tratamento
    Dado que Miguel Costa tem um ticket atribuído
    E o ticket está no estado "Aberto"
    Quando Miguel inicia o tratamento
    Então o estado passa para "Em tratamento"
    E a alteração fica registada no histórico

  Cenário: US-007 - Registar resolução
    Dado que Miguel Costa está a tratar um ticket atribuído
    E o estado é "Em tratamento"
    Quando regista a solução aplicada
    E indica que o problema foi resolvido
    Então o estado passa para "Resolvido"
    E a solução fica guardada no ticket

  Cenário: US-008 - Retomar um ticket resolvido
    Dado que Miguel Costa tem um ticket atribuído
    E o ticket está no estado "Resolvido"
    Quando Miguel indica que o problema persiste
    Então o estado volta a "Em tratamento"
    E a alteração fica registada no histórico

  Cenário: US-009 - Fechar um ticket
    Dado que Sofia Almeida acedeu como Responsável de TI
    E existe um ticket no estado "Resolvido"
    Quando Sofia fecha o ticket
    Então o estado passa para "Fechado"
    E o histórico permanece disponível

  Cenário: US-010 - Consultar histórico
    Dado que Sofia Almeida acedeu como Responsável de TI
    E existem alterações de estado num ticket
    Quando consulta o histórico desse ticket
    Então visualiza as alterações de estado e de técnico
    E visualiza a data e o utilizador de cada alteração
    E nas reatribuições visualiza os técnicos anterior e novo

  Cenário: US-011 - Iniciar sessão
    Dado que Ana Martins tem uma conta ativa
    E está associada ao perfil "Colaborador"
    Quando introduz o email e a palavra-passe corretos
    Então o sistema autentica Ana Martins
    E permite o acesso às funcionalidades do seu perfil

  Cenário: US-012 - Reatribuir um ticket
    Dado que Sofia Almeida iniciou sessão como Responsável de TI
    E existe um ticket "Em tratamento" atribuído a Miguel Costa
    Quando Sofia atribui o ticket a outro técnico
    Então o novo técnico passa a ser responsável pelo ticket
    E o estado permanece "Em tratamento"
    E a reatribuição fica registada no histórico

  # ==========================================
  # REGRAS DE TRANSIÇÃO
  # ==========================================

  Cenário: RT-001 - Impedir resolução direta
    Dado que existe um ticket no estado "Aberto"
    Quando é solicitada a alteração direta para "Resolvido"
    Então o sistema rejeita a alteração
    E o ticket permanece "Aberto"

  Cenário: RT-002 - Impedir fecho direto
    Dado que existe um ticket no estado "Aberto"
    Quando é solicitada a alteração direta para "Fechado"
    Então o sistema rejeita a alteração
    E o ticket permanece "Aberto"

  Cenário: RT-003 - Impedir fecho pelo técnico
    Dado que Miguel Costa acedeu como Técnico de suporte
    E existe um ticket no estado "Resolvido"
    Quando Miguel tenta fechar o ticket
    Então o sistema rejeita a operação
    E o ticket permanece "Resolvido"

  Cenário: RT-004 - Impedir reabertura de ticket fechado
    Dado que existe um ticket no estado "Fechado"
    Quando é solicitada a alteração para "Aberto"
    Então o sistema rejeita a alteração
    E o ticket permanece "Fechado"

  # ==========================================
  # PERMISSÕES E ACESSOS
  # ==========================================

  Cenário: RT-005 - Impedir acesso não autorizado
    Dado que Ana Martins acedeu como Colaborador
    E existe um ticket criado por outro colaborador
    Quando Ana tenta consultar esse ticket
    Então o sistema impede o acesso
    E apresenta uma mensagem de operação não autorizada

  Cenário: RT-006 - Acesso com perfil associado
    Dado que Ana Martins é uma utilizadora identificada
    E tem o perfil "Colaborador"
    Quando acede ao SmartDesk
    Então o sistema reconhece o seu perfil
    E disponibiliza apenas as operações autorizadas

  # ==========================================
  # VALIDAÇÃO DE CATEGORIAS
  # ==========================================

  Esquema do Cenário: RT-007 - Validar categorias
    Dado que Ana Martins está a criar um ticket
    Quando seleciona a categoria "<categoria>"
    Então o sistema aceita a categoria

    Exemplos:
      | categoria   |
      | Equipamento |
      | Software    |
      | Acessos     |

  Cenário: RT-008 - Rejeitar categoria inválida
    Dado que Ana Martins está a criar um ticket
    Quando tenta utilizar a categoria "Outros"
    Então o sistema rejeita a categoria
    E informa que a categoria não é permitida

  # ==========================================
  # RESOLUÇÃO E TRANSIÇÕES INVÁLIDAS
  # ==========================================

  Cenário: RT-009 - Impedir resolução sem solução
    Dado que Miguel Costa tem um ticket atribuído
    E o ticket está no estado "Em tratamento"
    Quando tenta alterar o estado para "Resolvido"
    E não regista uma solução
    Então o sistema rejeita a alteração
    E mantém o estado "Em tratamento"

  Esquema do Cenário: RT-010 - Rejeitar outras transições
    Dado que existe um ticket no estado "<origem>"
    Quando é solicitada a alteração para "<destino>"
    Então o sistema rejeita a alteração
    E mantém o estado "<origem>"

    Exemplos:
      | origem        | destino       |
      | Em tratamento | Aberto        |
      | Em tratamento | Fechado       |
      | Resolvido     | Aberto        |
      | Fechado       | Em tratamento |
      | Fechado       | Resolvido     |

  # ==========================================
  # CONSULTA E REQUISITOS NÃO FUNCIONAIS
  # ==========================================

  Cenário: RT-011 - Consultar por técnico e estado
    Dado que Sofia Almeida acedeu como Responsável de TI
    E existem tickets atribuídos a diferentes técnicos
    Quando consulta os tickets de Miguel Costa
    E seleciona o estado "Em tratamento"
    Então visualiza apenas os tickets que cumprem
    ambos os critérios

  Esquema do Cenário: RT-012 - Utilizar no Chrome e Edge
    Dado que o utilizador dispõe do navegador "<navegador>"
    Quando acede ao SmartDesk
    Então consegue iniciar sessão e utilizar a aplicação
    E não exige instalação de software adicional

    Exemplos:
      | navegador      |
      | Google Chrome  |
      | Microsoft Edge |

  Cenário: RT-013 - Verificar clareza da interface
    Dado que um colaborador participa num teste de utilização
    Quando cria e consulta um ticket sem ajuda
    Então consegue concluir ambas as tarefas
    E identifica corretamente o estado do ticket

  Cenário: RT-014 - Verificar persistência
    Dado que Miguel Costa registou a resolução de um ticket
    Quando termina a sessão
    E volta a aceder ao SmartDesk
    Então a resolução continua disponível
    E o histórico de alterações foi preservado

  Cenário: RT-015 - Mensagem de operação inválida
    Dado que Miguel Costa tem um ticket em tratamento
    Quando tenta alterar diretamente o estado para "Fechado"
    Então o sistema rejeita a operação
    E apresenta uma mensagem que explica a restrição
    E mantém o estado "Em tratamento"

  # ==========================================
  # VERIFICAÇÕES ADICIONAIS
  # ==========================================

  Cenário: RT-016 - Impedir tratamento por técnico não atribuído
    Dado que Miguel Costa acedeu como Técnico de suporte
    E existe um ticket no estado "Aberto"
    E o ticket está atribuído a outro técnico
    Quando Miguel tenta iniciar o tratamento
    Então o sistema rejeita a operação
    E o ticket permanece no estado "Aberto"
    E apresenta uma mensagem de operação não autorizada

  Esquema do Cenário: RT-017 - Validar campos obrigatórios
    Dado que Ana Martins está a criar um ticket
    E preenche corretamente os restantes campos
    Quando tenta submeter o ticket sem "<campo>"
    Então o sistema não cria o ticket
    E informa que o campo "<campo>" é obrigatório

    Exemplos:
      | campo     |
      | título    |
      | descrição |
      | categoria |

  Esquema do Cenário: RT-018 - Impedir alterações após fecho
    Dado que existe um ticket no estado "Fechado"
    E o utilizador tem o perfil "<perfil>"
    Quando tenta alterar o estado para "<destino>"
    Então o sistema rejeita a alteração
    E o ticket permanece no estado "Fechado"

    Exemplos:
      | perfil             | destino       |
      | Colaborador        | Aberto        |
      | Técnico de suporte | Em tratamento |
      | Responsável de TI  | Resolvido     |

  # AUTENTICAÇÃO

  Cenário: RT-019 - Rejeitar credenciais incorretas
    Dado que Ana Martins está na página de início de sessão
    Quando introduz uma palavra-passe incorreta
    Então o sistema impede o acesso
    E apresenta uma mensagem de autenticação inválida

  Cenário: RT-020 - Terminar sessão
    Dado que Ana Martins iniciou sessão no SmartDesk
    Quando termina a sessão
    Então o sistema encerra a sessão autenticada
    E impede o acesso às funcionalidades internas até novo início de sessão

  # REATRIBUIÇÃO

  Esquema do Cenário: RT-021 - Reatribuir nos estados permitidos
    Dado que Sofia Almeida iniciou sessão como Responsável de TI
    E existe um ticket no estado "<estado>" atribuído a Miguel Costa
    Quando Sofia reatribui o ticket a outro técnico
    Então o novo técnico fica responsável pelo ticket
    E o estado permanece "<estado>"
    E a alteração fica registada no histórico

    Exemplos:
      | estado        |
      | Aberto        |
      | Em tratamento |
      | Resolvido     |

  Cenário: RT-022 - Impedir reatribuição de ticket fechado
    Dado que Sofia Almeida iniciou sessão como Responsável de TI
    E existe um ticket no estado "Fechado"
    Quando tenta reatribuir o ticket a outro técnico
    Então o sistema rejeita a operação
    E mantém o técnico anteriormente atribuído
    E mantém o estado "Fechado"

  Esquema do Cenário: RT-023 - Impedir tratamento após reatribuição
    Dado que Sofia Almeida reatribuiu a outro técnico um ticket anteriormente atribuído a Miguel Costa
    E o ticket está no estado "<estado>"
    Quando Miguel tenta executar "<operacao>"
    Então o sistema rejeita a operação
    E mantém o estado "<estado>"

    Exemplos:
      | estado        | operacao           |
      | Aberto        | iniciar tratamento |
      | Em tratamento | registar resolução |
      | Resolvido     | retomar tratamento |
