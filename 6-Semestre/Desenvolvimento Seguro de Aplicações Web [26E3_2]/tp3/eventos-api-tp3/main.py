from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from sqlmodel import Session

from routes.eventos import router as eventos_router
from routes.auth import router as auth_router
from database.db import criar_tabelas, seed, engine
from middleware.security_headers import SecurityHeadersMiddleware
from middleware.rate_limit import limiter

app = FastAPI(
    title="eventos-api",
    description="API de eventos com controles defensivos OWASP Top 10",
    version="0.3.0",
)

# ── Rate limiting (Exercício 7) ───────────────────────────────────────────────
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ── CORS (Exercício 6) — allowlist explícita, SEM wildcard ───────────────────
# Em produção, substitua pela(s) origem(s) real(is) do seu frontend.
ALLOWED_ORIGINS = [
    "http://localhost:3000",        # frontend de desenvolvimento local
    "http://localhost:5173",        # Vite dev server
    "https://app.meudominio.com",   # frontend de produção
    "https://parceiro.xpto.com",    # parceiro externo autorizado
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,       # nunca usar ["*"] em produção
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# ── Cabeçalhos de segurança (Exercício 6) ────────────────────────────────────
app.add_middleware(SecurityHeadersMiddleware)

# ── Routers ───────────────────────────────────────────────────────────────────
app.include_router(auth_router)
app.include_router(eventos_router)


# ── Lifecycle ─────────────────────────────────────────────────────────────────
@app.on_event("startup")
def startup():
    criar_tabelas()
    with Session(engine) as session:
        seed(session)


@app.get("/", tags=["status"])
def status():
    return {"status": "ok", "servico": "eventos-api", "versao": "0.3.0"}
