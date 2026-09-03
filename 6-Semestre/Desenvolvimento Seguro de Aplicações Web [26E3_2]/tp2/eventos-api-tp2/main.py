from fastapi import FastAPI
from routes.eventos import router as eventos_router
from routes.auth import router as auth_router
import database.db as db

app = FastAPI(
    title="eventos-api",
    description="API de gerenciamento de eventos com autenticação JWT + RBAC",
    version="0.2.0",
)

app.include_router(auth_router)
app.include_router(eventos_router)


@app.on_event("startup")
def startup():
    db.seed()


@app.get("/", tags=["status"])
def status():
    return {"status": "ok", "servico": "eventos-api", "versao": "0.2.0"}
