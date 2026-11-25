# Setup do Ambiente — OpenAI Agents SDK (NeoStream TP3)

Este documento registra o passo a passo de configuração do ambiente virtual, instalação do OpenAI Agents SDK e gerenciamento seguro da chave de API da OpenAI sem versionar credenciais no repositório Git.

---

## 1. Pré-requisitos

- Python 3.10 ou superior (ambiente testado com **Python 3.13.5**).
- Acesso à internet para instalação dos pacotes via `pip` e comunicação com a API da OpenAI.
- Chave de API válida da OpenAI fornecida para o ambiente de testes.

---

## 2. Criação e ativação do ambiente virtual

Na pasta do projeto (`tp3`), crie um ambiente virtual isolado para evitar conflitos com pacotes globais do sistema:

```powershell
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instalação das dependências e registro em `requirements.txt`

Com o ambiente virtual ativado, instale o SDK oficial (`openai-agents`) e a biblioteca `python-dotenv`:

```powershell
python -m pip install --upgrade pip
pip install openai-agents python-dotenv
```

As versões instaladas e fixadas em `requirements.txt` são:

```text
openai-agents==0.26.0
python-dotenv==1.2.4
pydantic==2.14.4
```

Para reproduzir exatamente o mesmo ambiente em outra máquina:

```powershell
pip install -r requirements.txt
```

---

## 4. Configuração segura da API key com `.env` e `.gitignore`

Para seguir as boas práticas de segurança e impedir qualquer vazamento da chave no Git ou no pacote de entrega:

1. **Modelo sem segredos (`.env.example`):** mantém apenas o nome da variável e um valor fictício para documentar o formato esperado:
   ```env
   OPENAI_API_KEY=sk-proj-substitua-pela-sua-chave-aqui
   ```
2. **Arquivo local com a chave real (`.env`):** copie `.env.example` para `.env` e substitua pelo token real da OpenAI:
   ```powershell
   Copy-Item .env.example .env
   ```
3. **Proteção no Git (`.gitignore`):** garanta que `.env`, `.venv/` e arquivos temporários estejam explicitamente ignorados:
   ```gitignore
   .env
   .env.*
   !.env.example
   .venv/
   __pycache__/
   ```
4. **Carregamento no código:** todos os scripts carregam as variáveis em tempo de execução com `from dotenv import load_dotenv; load_dotenv()`, sem nunca escrever a chave em código-fonte, logs ou documentos.

---

## 5. Verificação do ambiente

Execute o script `verificar_ambiente.py` para confirmar, sem expor a chave, que a variável `OPENAI_API_KEY` está carregada e que o `OpenAIProvider` do SDK consegue inicializar o cliente corretamente:

```powershell
python verificar_ambiente.py
```

Saída obtida na validação local do ambiente:

```text
[OK] OPENAI_API_KEY carregada via ambiente/.env (comprimento: 53 caracteres; valor oculto).
[OK] OpenAI Agents SDK importado (versão 0.26.0).
[OK] OpenAIProvider inicializado e pronto para uso com o modelo 'gemini-3.6-flash'.
Ambiente validado com sucesso.
```

> **Nota de portabilidade:** os scripts usam o `openai-agents` SDK de forma nativa com a API da OpenAI (bastando definir `OPENAI_API_KEY` no `.env`). Opcionalmente, caso se deseje testar em ambiente sem créditos OpenAI usando um endpoint compatível (como Google AI Studio / Gemini), basta informar `OPENAI_BASE_URL` e `OPENAI_DEFAULT_MODEL` no `.env`, conforme documentado em `.env.example`, sem alterar o código dos agentes.

Caso `.env` não exista ou ainda contenha o valor de exemplo, o script encerra com código de saída `1` indicando o ajuste necessário.
