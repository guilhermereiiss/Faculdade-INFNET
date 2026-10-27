from routes.auth import router as auth_router
from routes.consultas import router as consultas_router
from routes.pacientes import router as pacientes_router
from routes.profissionais import router as profissionais_router
from routes.recepcao import router as recepcao_router
from routes.laboratorio import router as laboratorio_router

__all__ = [
    "auth_router",
    "consultas_router",
    "pacientes_router",
    "profissionais_router",
    "recepcao_router",
    "laboratorio_router",
]
