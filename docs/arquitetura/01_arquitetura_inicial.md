# Passo 6 — Arquitetura inicial do SmartDesk

**Estado:** Proposta aprovada. **Âmbito:** MVP com 12 User Stories, três perfis, três categorias e quatro estados.

## 1. Arquitetura proposta

Aplicação web simples com três componentes lógicos:

```text
┌─────────────────────────────────────────────────────────────┐
│ FRONTEND — Interface web (Ana, Miguel e Sofia)              │
│ Formulários, listas, estados e ações permitidas             │
└──────────────────────────┬──────────────────────────────────┘
                           │ Pedidos e respostas HTTP
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ BACKEND — Regras do SmartDesk                                │
│ Autenticação, permissões, gestão de tickets, validações     │
│ e transições de estado                                      │
└──────────────────────────┬──────────────────────────────────┘
                           │ Leitura e gravação
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ BASE DE DADOS                                               │
│ Utilizadores, tickets, atribuições e resoluções             │
└─────────────────────────────────────────────────────────────┘
```

## 2. Papel de cada componente

| Componente | Responsabilidade | Exemplo |
|---|---|---|
| Frontend | Apresentar páginas, formulários e informação. | Ana preenche o formulário de um novo ticket. |
| Backend | Receber pedidos, validar dados e aplicar permissões e regras de negócio. | Verificar que apenas Sofia pode fechar um ticket. |
| Base de dados | Guardar informação necessária ao funcionamento. | Conservar o estado, categoria e técnico responsável. |

O frontend pode apresentar as ações permitidas, mas **é o backend que deve fazer cumprir as permissões**, mesmo que alguém tente realizar uma operação diretamente.

## 3. Tecnologias propostas

| Camada | Tecnologia | Justificação |
|---|---|---|
| Frontend | HTML, CSS e templates simples | Interface web sem necessidade de uma framework JavaScript complexa. |
| Backend | Python com FastAPI | Organização das operações e validação de pedidos. |
| Base de dados | SQLite | Não exige um servidor de base de dados separado. |

Na primeira versão, o frontend e o backend podem executar-se na mesma aplicação, embora mantenham responsabilidades distintas. Não se propõem React, Kubernetes, microsserviços, filas ou infraestrutura cloud: não são necessários para demonstrar o MVP.

## 4. Informação essencial a guardar

| Entidade | Dados principais |
|---|---|
| Utilizador | Identificador, nome, email, credencial de autenticação protegida e perfil. |
| Ticket | Identificador, título, descrição, categoria, estado e colaborador criador. |
| Atribuição | Técnico atualmente responsável pelo ticket. |
| Resolução | Descrição da solução aplicada pelo técnico. |

As palavras-passe não devem ser guardadas em texto simples. O mecanismo concreto de proteção será definido na implementação.

## 5. Exemplo de funcionamento

1. O frontend apresenta o formulário de novo ticket a Ana.
2. Ana introduz título, descrição e categoria **Equipamento**.
3. O backend valida a autenticação e os campos obrigatórios.
4. A base de dados guarda o ticket no estado **Aberto**.
5. O frontend apresenta o ticket criado.

O mesmo princípio aplica-se às operações de Miguel e Sofia.

## 6. Regras e limites

- **Perfis:** colaborador (Ana Martins), técnico (Miguel Costa) e responsável de TI (Sofia Almeida).
- **Categorias:** Equipamento, Software e Acessos.
- **Estados:** Aberto, Em tratamento, Resolvido e Fechado.
- Sofia pode atribuir e reatribuir tickets, incluindo os que estão Em tratamento.
- Ana pode comunicar que um problema persiste, fazendo o ticket regressar de Resolvido a Em tratamento.
- Apenas Sofia pode fechar tickets Resolvidos, após confirmação da resolução.
- Um ticket Fechado não pode ser reaberto.
- O objetivo de resposta até **3 segundos** é provisório e carece de medição em condições definidas.
- A compatibilidade será verificada no Chrome e no Edge, em computador.

**Fora do MVP:** aplicação móvel, SMS, integração automática com email, resolução por IA e SLA avançado.

**Não definidos nesta etapa:** Docker, redes internas, volumes, PostgreSQL, CI/CD e cloud. Poderão ser abordados posteriormente sem alterar os requisitos de negócio.

**Referências internas:** [Requisitos e User Stories](../produto/02_requisitos_e_user_stories.md), [MVP e backlog](../produto/03_mvp_backlog_e_aceitacao.md), [Testes e rastreabilidade](../qualidade/01_testes_e_rastreabilidade.md).
