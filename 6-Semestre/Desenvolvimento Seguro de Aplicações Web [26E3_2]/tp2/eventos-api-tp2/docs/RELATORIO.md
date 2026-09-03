# Relatório técnico — eventos-api TP2

> **Disciplina:** Programação Distribuída e Redes com Linux e Python  
> **Turma:** 26E1_5 — Instituto Infnet  
> **Professor:** Ricardo Pires  
> **Aluno:** Guilherme Reis

---

## Visão geral

Este relatório documenta as decisões técnicas do TP2, construído sobre o `eventos-api` do TP1. Os exercícios cobrem threat modeling com STRIDE, misuse cases, e implementação de autenticação JWT com bcrypt, MFA e RBAC por escopos OAuth 2.0.

---

## Exercício 1 — Misuse Cases

Quatro misuse cases priorizados por impacto (maior → menor):

| # | Ator malicioso | Ação indesejada | Impacto | Vetor no TP1 |
|---|---|---|---|---|
| 1 | Atacante externo | Enumeração de organizadores via `POST /eventos/inseguro/criar` | Alto — expõe `organizador_id` sequencial, permite mapear toda a base de usuários | Ausência de `response_model` na rota de demonstração |
| 2 | Usuário autenticado | Editar ou deletar evento de outro usuário | Alto — violação de integridade dos dados de terceiros | Ausência de verificação de ownership nas rotas de escrita |
| 3 | Atacante externo | Flood de `POST /eventos/` até esgotar memória do processo | Médio — derruba o serviço para todos os usuários (DoS) | Ausência de rate limiting na API |
| 4 | Usuário mal-intencionado | Injetar `<script>` no nome de um evento para executar XSS nos navegadores de outros usuários | Médio — mitigado pelo Jinja2 auto-escape, mas possível via resposta JSON consumida por frontend sem sanitização | Dado aceito pela API sem validação de conteúdo além do tipo |

**Justificativa da ordem:** os dois primeiros expõem dados de terceiros (impacto direto sobre confidencialidade e integridade de outros usuários). O terceiro afeta disponibilidade do serviço inteiro. O quarto é mitigado em parte pelo Jinja2 mas permanece como risco em clientes JSON.

---

## Exercício 2 — STRIDE

| Componente | Categoria STRIDE | Ameaça identificada |
|---|---|---|
| Rota `POST /eventos/` (sem auth no TP1) | **S**poofing | Qualquer cliente se passa por organizador legítimo sem apresentar credencial |
| Rota `PUT /eventos/{id}` (sem ownership) | **T**ampering | Usuário autenticado altera dados de evento que não é seu |
| Rota `POST /eventos/inseguro/criar` | **I**nformation Disclosure | `organizador_id` e `token_auditoria` retornados sem filtro |
| Banco em memória (sem log) | **R**epudiation | Nenhuma operação é registrada; impossível auditar quem criou ou alterou um evento |
| API sem rate limiting | **D**enial of Service | Flood de requisições esgota memória ou CPU do processo |
| Ausência de controle de papel nas rotas | **E**levation of Privilege | Participante consegue criar evento usando rota `POST /eventos/` se autenticado |

---

## Exercício 3 — Threat Model completo

### Ativos principais

| Ativo | Classificação | Localização |
|---|---|---|
| Dados de eventos (nome, data, local) | Confidencial — público após publicação | `database/db.py` em memória |
| Dados de organizadores (`organizador_id`) | Confidencial — interno | `database/db.py`, campo `EventoInterno` |
| Token de auditoria | Sensível — interno | `database/db.py`, campo `EventoInterno` |
| Credenciais de usuário (senha) | Crítico | `database/db.py` — armazenado como hash bcrypt |
| JWT de sessão | Crítico | Emitido por `auth/security.py`, trafega no header `Authorization` |

### Superfícies de ataque

- Endpoints públicos (sem auth): `GET /`, `POST /auth/login`, `POST /auth/registrar`
- Endpoints autenticados: `POST /eventos/`, `PUT /eventos/{id}`, `DELETE /eventos/{id}`
- Endpoint de demonstração: `POST /eventos/inseguro/criar` (intencionalmente inseguro)
- Endpoint MFA: `POST /auth/mfa/verificar`
- Endpoint M2M: `POST /auth/m2m/token`

### Ameaças e mitigações

| Ameaça (STRIDE) | Mitigação implementada | Status |
|---|---|---|
| Spoofing — acesso sem credencial | `OAuth2PasswordBearer` exige JWT válido em toda rota protegida | ✅ Implementado |
| Tampering — edição de evento alheio | `verificar_ownership()` compara `owner_username` do evento com o `sub` do token | ✅ Implementado |
| Information Disclosure — campos internos | `response_model=EventoResponse` filtra `organizador_id` e `token_auditoria` | ✅ Implementado (TP1) |
| Repudiation — sem rastro de operações | Claims `sub` e `iat` no JWT permitem rastrear quem fez o quê e quando | ⚠️ Parcial — JWT rastreia, mas não há log persistente |
| DoS — flood de requisições | Sem rate limiting implementado | ❌ Lacuna aberta |
| Elevation of Privilege — papel indevido | RBAC via escopos OAuth: `participante` só tem `eventos:read`, sem acesso a write | ✅ Implementado |

---

## Exercício 4 — Fronteiras de segurança e partições

### Partições do sistema

```
┌─────────────────────────────────────────────────────────────┐
│  Zona não confiável                                          │
│  ┌──────────────┐    ┌────────────────────┐                  │
│  │   Navegador  │    │  Parceiro M2M       │                  │
│  │  (usuário)   │    │  (client_id/secret) │                  │
│  └──────┬───────┘    └────────┬───────────┘                  │
└─────────┼───────────────────┼─────────────────────────────── ┘
          │  TB1 → validação JWT / credenciais                  
┌─────────▼───────────────────▼─────────────────────────────── ┐
│  Zona confiável — FastAPI                                      │
│  ┌─────────────────┐   ┌────────────────────────────────────┐ │
│  │  auth/ (JWT,    │   │  routes/eventos.py                 │ │
│  │  bcrypt, MFA,   │   │  + auth/dependencies.py            │ │
│  │  M2M)           │   │  (ownership, escopos)              │ │
│  └────────┬────────┘   └───────────────┬────────────────────┘ │
│           │  TB2 → dados já validados  │                       │
│  ┌────────▼────────────────────────────▼────────────────────┐ │
│  │  database/db.py — banco em memória                        │ │
│  └───────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

**TB1 — Trust boundary de entrada:** toda requisição externa atravessa a validação de JWT (rota `get_usuario_atual`) ou validação de credenciais M2M (`/auth/m2m/token`). Input não validado nunca alcança o banco.

**TB2 — Trust boundary interna:** o banco recebe apenas dados já validados pelo Pydantic e com ownership verificado. Campos internos (`organizador_id`, `token_auditoria`) nunca cruzam TB1 de volta ao cliente graças ao `response_model`.

**Como essa visão refina o threat model:** a análise de partições deixa claro que a maior superfície de risco está em TB1 — qualquer falha na validação de JWT ou na checagem de escopos permite que um cliente não autorizado alcance o banco. O threat model do Exercício 3 focava em ameaças por endpoint; a visão de partições revela que adicionar rate limiting em TB1 (antes de qualquer processamento) é mais eficaz do que em cada rota individualmente, pois protege todas as partições internas de uma vez.

---

## Exercício 5 — Três eixos de segurança para abertura a parceiros externos

| Eixo | Vetor de ataque | Coberto no threat model? |
|---|---|---|
| **Design** | API sem versionamento: parceiro externo consome `v1`, uma atualização quebra o contrato e expõe dados não previstos | ❌ Lacuna nova — o threat model atual não cobre riscos de evolução de contrato |
| **Implementação** | Escopos OAuth insuficientemente granulares: parceiro M2M com `m2m:write` poderia criar eventos em nome de qualquer organizador se não houver claim `client_id` separado | ⚠️ Parcial — mitigado no Exercício 8 com `client_id` no payload, mas não documentado no threat model |
| **Infraestrutura** | Serviço exposto sem TLS: JWT trafega em texto claro, permitindo interceptação e reutilização do token em redes intermediárias | ❌ Lacuna nova — a API roda em HTTP puro; HTTPS não está configurado |

**Por que considerar os três eixos?** Focar apenas em implementação (validação de token, bcrypt) resolve ameaças de camada de aplicação, mas deixa abertas falhas de design (contrato mal definido com o parceiro) e de infraestrutura (token interceptável sem TLS). Um parceiro externo amplia a superfície de ataque nos três eixos simultaneamente — o contrato define o que ele pode fazer (design), o código define como (implementação), e a rede define por onde os dados trafegam (infraestrutura).

---

## Exercício 6 — Autenticação OAuth2 + bcrypt + ownership

**Implementação:**  
- `passlib[bcrypt]` com `CryptContext` para hashing de senhas — senhas nunca armazenadas em texto plano
- `OAuth2PasswordBearer` com `tokenUrl="/auth/login"` como esquema de autenticação
- Dependency injection via `Security(get_usuario_atual, scopes=[...])` em cada rota protegida
- `verificar_ownership()` compara `evento.owner_username` com o `sub` do JWT antes de permitir edição

**Evidências de teste:**

```
# Login organizador
POST /auth/login  →  200  |  mfa_pendente: False

# Criar evento (autenticado como "gui")
POST /eventos/    →  201  |  id: 4

# Editar como DONO (gui editando evento de gui)
PUT /eventos/4    →  200  →  "Conf Editada"

# Editar como NÃO-DONO (joao tentando editar evento de gui)
PUT /eventos/4    →  403  →  "Escopo insuficiente: 'eventos:write' necessário"
```

> Nota: o usuário `joao` tem papel `participante`, que só recebe o escopo `eventos:read` — portanto é barrado antes mesmo da checagem de ownership.

---

## Exercício 7 — JWT com MFA e modelo de autorização

**Implementação do MFA:**  
Administradores têm `mfa_habilitado=True`. No login, recebem um token com escopo reduzido (`eventos:read`) e flag `mfa_pendente: true`. Para obter o token completo com `admin:all`, precisam chamar `POST /auth/mfa/verificar` com o código correto (simulado: `"123456"`; em produção seria `pyotp.TOTP`).

**Evidências de teste:**

```
# Login admin (MFA pendente)
POST /auth/login  →  200  |  mfa_pendente: True

# MFA código correto
POST /auth/mfa/verificar  {"codigo_mfa": "123456"}  →  200  (token completo emitido)

# MFA código errado
POST /auth/mfa/verificar  {"codigo_mfa": "000000"}  →  401  "Código MFA inválido"
```

**Comparação RBAC × ABAC × por recurso:**

| Modelo | Como funciona | Trade-off |
|---|---|---|
| **RBAC** | Permissões atribuídas a papéis fixos (`organizador`, `participante`, `admin`) | Simples de implementar e auditar; inflexível quando regras dependem de contexto |
| **ABAC** | Permissões avaliadas por atributos do usuário, do recurso e do ambiente | Flexível para regras complexas; difícil de auditar e depurar |
| **Por recurso** | Cada recurso define quem pode acessá-lo (ex: `owner_username`) | Granular e intuitivo; escala bem em sistemas com ownership claro |

**Recomendação para o eventos-api:** combinação de **RBAC + ownership por recurso**. RBAC define o que cada papel pode fazer em nível de escopo (`eventos:write` só para organizadores e admins); ownership por recurso define qual instância específica cada usuário pode modificar. Exemplo concreto: um organizador com `eventos:write` só pode editar os eventos em que `owner_username == sub` do token — outro organizador não consegue editar eventos alheios mesmo tendo o mesmo papel.

---

## Exercício 8 — OAuth 2.0 M2M e escopos

**Fluxo escolhido: Client Credentials Grant**  
Justificativa: o parceiro externo é uma máquina (sem usuário humano no fluxo). O `Authorization Code Grant` (usado para usuários finais) exige redirecionamento de navegador e consentimento — inadequado para integrações automatizadas. O `Client Credentials Grant` autentica diretamente com `client_id` + `client_secret` e emite token com os escopos contratados, sem interação humana.

**Comparação dos payloads JWT:**

Token de um **organizador** (Authorization Code / Password Grant):
```json
{
  "sub": "gui",
  "papel": "organizador",
  "scope": "eventos:read eventos:write eventos:delete"
}
```

Token do **parceiro M2M** (Client Credentials Grant):
```json
{
  "sub": "parceiro-externo",
  "papel": "m2m_parceiro",
  "scope": "m2m:read",
  "client_id": "parceiro-externo",
  "grant_type": "client_credentials"
}
```

**Diferenças-chave:**
- `grant_type: client_credentials` identifica o fluxo M2M — útil para logs de auditoria
- `client_id` no payload permite rastrear qual parceiro fez qual operação
- Escopo limitado a `m2m:read` / `m2m:write` — nunca `admin:all` ou `eventos:delete`
- Mesmo que o token M2M seja comprometido, o atacante só consegue executar as operações no escopo concedido — não consegue deletar eventos nem acessar dados administrativos

**Escopos configurados:**

| Escopo | Organizador | Participante | Admin | Parceiro M2M |
|---|---|---|---|---|
| `eventos:read` | ✅ | ✅ | ✅ | ❌ |
| `eventos:write` | ✅ | ❌ | ✅ | ❌ |
| `eventos:delete` | ✅ | ❌ | ✅ | ❌ |
| `admin:all` | ❌ | ❌ | ✅ | ❌ |
| `m2m:read` | ❌ | ❌ | ❌ | ✅ |
| `m2m:write` | ❌ | ❌ | ❌ | ✅ |

---

*eventos-api v0.2.0 — Guilherme Reis*
