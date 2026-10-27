# Roteiro de Apresentação em Vídeo (Até 5 Minutos)
## Assessment (AT) — Desenvolvimento Seguro de Aplicações Web
**Estudante:** Guilherme Reis  
**Objetivo:** Demonstração prática do código rodando, explicação das decisões técnicas de segurança, critério de severidade do Security Gate (Exercício 12) e auditoria final Capstone (Exercício 13).

---

## ⏱️ Cronograma Minuto a Minuto

```text
00:00 - 00:45 | 1. Abertura, Contexto e Arquitetura do Sistema
00:45 - 01:45 | 2. Demonstração Prática: Execução dos Testes Pytest (23 Testes)
01:45 - 02:45 | 3. Segurança no Código: Anti-BOLA, Ownership Check e Pydantic extra='forbid'
02:45 - 03:45 | 4. Exercício 12: DevSecOps Pipeline e Critério do Security Gate
03:45 - 04:45 | 5. Exercício 13: Auditoria Capstone, ZAP Scan e Risco Residual
04:45 - 05:00 | 6. Encerramento e Entrega
```

---

## 📝 Fala Sugerida & O que Mostrar na Tela

### 1. Abertura e Contexto (00:00 - 00:45)
- **O que mostrar:** Seu rosto ou tela com o VS Code / IDE aberto na pasta `AT`, mostrando a árvore de diretórios modular (`routes`, `models`, `database`, `auth`, `middleware`, `templates`, `tests`).
- **O que falar:**
  > "Olá, professor e avaliadores! Meu nome é Guilherme Reis e esta é a apresentação do meu Assessment de Desenvolvimento Seguro de Aplicações Web.
  > Neste projeto, construí do zero uma API REST corporativa de agendamento de consultas médicas voltada para conformidade rigorosa com a LGPD e tratamento de dados sensíveis de saúde.
  > A aplicação atende três tipos de clientes: uma aplicação frontend JSON, uma página HTML interna da recepção com Jinja2 protegida contra XSS, e uma integração máquina-a-máquina (M2M) com um laboratório parceiro via OAuth 2.0 Client Credentials."

---

### 2. Demonstração Prática: Execução dos Testes (00:45 - 01:45)
- **O que mostrar:** Abra o terminal e digite:
  ```powershell
  .\.venv\Scripts\python.exe -m pytest tests -v
  ```
  Mostre os 23 testes passando em verde no terminal.
- **O que falar:**
  > "Para demonstrar o funcionamento prático, estou rodando a nossa suíte de testes automatizados com o Pytest.
  > Como podem ver na tela, temos 23 testes automatizados passando com 100% de sucesso.
  > Esses testes cobrem desde a fundação da API no Exercício 1, controle de exposição de campos no Exercício 2, autenticação com MFA e bloqueio de usuários comuns em rotas administrativas com 403 Forbidden no Exercício 6, segregação de escopos M2M no Exercício 7, até os vetores do OWASP Top 10 como BOLA, Mass Assignment e SQL Injection."

---

### 3. Destaques de Segurança no Código (01:45 - 02:45)
- **O que mostrar:** 
  1. Abra o arquivo `auth/dependencies.py` na função `verificar_ownership_consulta`.
  2. Abra `models/consulta.py` mostrando `model_config = ConfigDict(extra='forbid')` e o response model `ConsultaResponse`.
- **O que falar:**
  > "Vou destacar duas decisões centrais de código:
  > Primeiro, para combater o BOLA (Broken Object Level Authorization - OWASP API1:2023), implementamos a função `verificar_ownership_consulta`. Ela assegura que um médico só consiga acessar e alterar prontuários das suas próprias consultas. Se ele tentar trocar o ID na URL, a API retorna imediatamente HTTP 403 Forbidden.
  > Segundo, em todos os modelos de entrada, como `ConsultaCreate` e `PacienteCreate`, utilizamos `extra='forbid'` do Pydantic v2. Isso elimina totalmente a vulnerabilidade de Mass Assignment (API3:2023), pois qualquer campo não autorizado injetado pelo atacante é sumariamente rejeitado com erro 422."

---

### 4. Exercício 12: Pipeline DevSecOps e Security Gate (02:45 - 03:45)
- **O que mostrar:** Abra o arquivo `.github/workflows/security.yml`.
- **O que falar:**
  > "No Exercício 12, estruturamos o pipeline de DevSecOps no GitHub Actions com quatro etapas:
  > 1. Análise Estática com Bandit (SAST);
  > 2. Análise de Dependências com Pip-Audit (SCA);
  > 3. Testes Automatizados com Pytest;
  > 4. E o Security Gate consolidado.
  > 
  > O nosso critério de severidade para o Security Gate é: **bloqueio imediato do pipeline para qualquer vulnerabilidade de severidade HIGH (Alta) ou CRITICAL (Crítica)**.
  > A justificativa técnica para esse critério é que estamos tratando de dados médicos sensíveis protegidos pela LGPD. Uma falha de severidade Alta ou Crítica — como um bypass de autorização ou uma injeção de comandos — causaria vazamento direto de prontuários ou sequestro do banco de dados. Portanto, a tolerância para severidades Alta e Crítica em ambiente produtivo é zero."

---

### 5. Exercício 13: Capstone, ZAP Scan e Risco Residual (03:45 - 04:45)
- **O que mostrar:** Abra `zap_scan_report.json` ou `RELATORIO_TECNICO_AT.md` na seção da Matriz de Rastreabilidade.
- **O que falar:**
  > "No Exercício 13, fechamos o Capstone com uma auditoria completa de ponta a ponta:
  > Realizamos o scan passivo baseado nas regras do OWASP ZAP, confirmando a presença de todos os cabeçalhos de hardening: HSTS por 1 ano, CSP, X-Frame-Options DENY contra clickjacking e X-Content-Type-Options nosniff.
  > Construímos uma matriz de rastreabilidade completa que correlaciona cada ameaça do Threat Model STRIDE do Exercício 4 à vulnerabilidade OWASP, ao código de correção e à evidência de teste.
  > 
  > Sobre os riscos residuais: identificamos a presença de timestamps Unix legíveis nos claims JWT e a documentação Swagger em `/docs`. Avaliamos que o timestamp é padrão do RFC 7519 e não traz risco à aplicação, e que a rota `/docs` pode ser facilmente desativada em produção configurando `docs_url=None`. Sendo assim, o risco residual é perfeitamente aceitável e a aplicação está formalmente **aprovada e liberada para deploy**."

---

### 6. Encerramento (04:45 - 05:00)
- **O que falar:**
  > "Todo o código-fonte, o relatório técnico detalhado e as evidências estão empacotados no arquivo ZIP da entrega. Agradeço a atenção e fico à disposição para quaisquer dúvidas!"

---

## 📌 Checklist Rápido antes de Gravar:
- [ ] Subir o vídeo no YouTube como **Não Listado** (Unlisted).
- [ ] Copiar o link gerado e colar no seu documento de entrega/resposta do AT.
- [ ] Conferir se o áudio está limpo e a tela legível em 1080p.
