from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from sqlmodel import Session

from config import settings
from database.db import engine, criar_tabelas, seed
from middleware.rate_limit import limiter
from middleware.security_headers import SecurityHeadersMiddleware

from routes.auth import router as auth_router
from routes.consultas import router as consultas_router
from routes.pacientes import router as pacientes_router
from routes.profissionais import router as profissionais_router
from routes.recepcao import router as recepcao_router
from routes.laboratorio import router as laboratorio_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Inicialização segura do banco de dados e dados padrão (seed).
    """
    criar_tabelas()
    with Session(engine) as session:
        seed(session)
    yield


app = FastAPI(
    title="API de Agendamento de Consultas — Clínica Médica Segura",
    description=(
        "API REST com arquitetura modular defensiva, conformidade LGPD para dados de saúde, "
        "autenticação OAuth2/JWT com MFA, integração M2M via Client Credentials, "
        "mitigação de OWASP Top 10 (Anti-BOLA, Mass Assignment, Injection) e Security Headers."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# ── 1. Rate Limiting (Exercício 10) ───────────────────────────────────────────
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ── 2. CORS com Allowlist Explícita (Exercício 10) — SEM WILDCARD ─────────────
# O time de segurança e auditores exigem que nenhuma origem com wildcard (*) seja utilizada
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-MFA-Code"],
)

# ── 3. Cabeçalhos de Segurança HTTP (Exercício 10) ────────────────────────────
# Injeta HSTS, X-Frame-Options (DENY), X-Content-Type-Options (nosniff) e CSP
app.add_middleware(SecurityHeadersMiddleware)

# ── 4. Roteadores Modulares (Exercício 1, 2, 6, 7) ────────────────────────────
app.include_router(auth_router)
app.include_router(consultas_router)
app.include_router(pacientes_router)
app.include_router(profissionais_router)
app.include_router(recepcao_router)
app.include_router(laboratorio_router)


@app.get("/", tags=["Status"])
def root():
    return {
        "status": "online",
        "servico": "clinica-medica-agendamento-api",
        "versao": "1.0.0",
        "seguranca": {
            "hsts": "ativo",
            "cors": "allowlist_estrita",
            "mfa_admin": "obrigatorio",
            "anti_bola": "ativo",
            "lgpd": "conformidade_dados_sensiveis",
        },
    }
