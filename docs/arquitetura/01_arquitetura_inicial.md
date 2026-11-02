# 6. Arquitetura Inicial do SmartDesk

## 6.1. Objetivo

Definir uma arquitetura simples para implementar o MVP do SmartDesk, suportando as 12 User Stories e os requisitos aprovados.

## 6.2. Visão geral

O SmartDesk utilizará uma arquitetura de três camadas:

```text
Utilizadores (Chrome / Edge)
             |
             v
          Frontend
             |
        API HTTPS/JSON
             |
             v
          Backend
             |
             v
        Base de dados
```

O frontend comunica com o backend através de uma API. Apenas o backend acede diretamente à base de dados.

## 6.3. Componentes e responsabilidades

### Frontend

Interface web utilizada pelos três perfis do SmartDesk.

Responsabilidades:

- Apresentar a página de autenticação.
- Permitir criar e consultar tickets.
- Apresentar os estados e as resoluções.
- Disponibilizar as operações de atribuição e reatribuição.
- Apresentar o histórico.
- Permitir terminar sessão.
- Apresentar mensagens de erro e validação.

Deve funcionar no Google Chrome e Microsoft Edge.

O frontend pode adaptar a interface ao perfil, mas não é responsável por garantir as permissões.

### Backend

Aplicação central responsável pelas regras de negócio.

Responsabilidades:

- Autenticar utilizadores por email e palavra-passe.
- Gerir sessões e verificar permissões.
- Criar e consultar tickets.
- Atribuir e reatribuir técnicos.
- Validar transições de estado.
- Exigir uma solução para resolver tickets.
- Impedir alterações não autorizadas.
- Registar históricos.
- Comunicar com a base de dados.

A autorização deve ser verificada em cada operação no backend.

### Base de dados

Armazena de forma persistente:

| Entidade | Informação |
|---|---|
| Utilizadores | Identificador, email, palavra-passe protegida e perfil |
| Tickets | Identificador, título, descrição, categoria, autor, data, estado, técnico atribuído e solução |
| Histórico | Ticket, tipo de alteração, data, utilizador, valores anteriores e novos |

As palavras-passe nunca devem ser guardadas em texto legível.

## 6.4. Funcionamento de uma operação

1. O utilizador executa uma ação no frontend.
2. O frontend envia o pedido ao backend.
3. O backend verifica a autenticação e as permissões.
4. O backend valida as regras de negócio.
5. O backend consulta ou atualiza a base de dados.
6. O resultado é devolvido ao frontend.

**Exemplo:** quando Sofia reatribui um ticket, o backend verifica que o ticket não está Fechado, atualiza o técnico responsável sem alterar o estado e regista a operação no histórico.

## 6.5. Decisões técnicas iniciais

| Aspeto | Decisão | Justificação |
|---|---|---|
| Arquitetura | Três camadas | Separação simples de responsabilidades |
| Frontend | Aplicação web | Acesso pelo Chrome e Edge |
| Backend | Aplicação única e modular | Evitar complexidade desnecessária |
| Comunicação | API HTTP/JSON sobre HTTPS | Comunicação estruturada e segura |
| Base de dados | Relacional | Adequada às relações entre utilizadores, tickets e histórico |
| Autenticação | Email e palavra-passe próprios | Conforme o MVP aprovado |
| Execução inicial | Ambiente local | Facilita desenvolvimento e demonstração |

Não serão utilizados microserviços, Kubernetes ou componentes distribuídos no MVP.

## 6.6. Limites e evolução

Esta arquitetura suporta:

- Os três perfis aprovados.
- As três categorias de tickets.
- Os quatro estados.
- Atribuição e reatribuição de técnicos.
- Autenticação e permissões.
- Histórico e persistência.

A escolha concreta das linguagens, frameworks, base de dados e ferramentas de execução será justificada antes da implementação.

Os testes e a respetiva rastreabilidade estão documentados em `docs/qualidade/01_testes_e_rastreabilidade.md`.
