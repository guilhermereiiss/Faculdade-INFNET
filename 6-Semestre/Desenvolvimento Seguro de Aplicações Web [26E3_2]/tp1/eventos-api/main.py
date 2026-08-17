from fastapi import FastAPI
from routes.eventos import router as eventos_router
import database.db as db

app = FastAPI(
    title="eventos-api",
    description="API de gerenciamento de inscrições em eventos",
    version="0.1.0",
)

# Registra o router de eventos — main.py não contém rotas de domínio
app.include_router(eventos_router)


@app.on_event("startup")
def startup():
    db.seed()  # popula o banco com dados de exemplo


@app.get("/", tags=["status"])
def status():
    """Rota de health check — valida que o serviço está acessível."""
    return {"status": "ok", "servico": "eventos-api", "versao": "0.1.0"}
