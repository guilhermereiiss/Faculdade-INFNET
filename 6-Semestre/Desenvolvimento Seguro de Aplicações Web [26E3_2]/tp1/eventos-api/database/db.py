import uuid
from models.evento import EventoCreate, EventoInterno

# Banco de dados simulado em memória
_db: dict[int, EventoInterno] = {}
_next_id = 1


def listar_eventos() -> list[EventoInterno]:
    return list(_db.values())


def obter_evento(evento_id: int) -> EventoInterno | None:
    return _db.get(evento_id)


def criar_evento(dados: EventoCreate) -> EventoInterno:
    global _next_id
    evento = EventoInterno(
        **dados.model_dump(),
        id=_next_id,
        organizador_id=f"ORG-{_next_id:04d}",       # ID interno — não deve vazar
        token_auditoria=str(uuid.uuid4()),             # token interno — não deve vazar
    )
    _db[_next_id] = evento
    _next_id += 1
    return evento


def deletar_evento(evento_id: int) -> bool:
    if evento_id in _db:
        del _db[evento_id]
        return True
    return False


# Seeds para demonstração (Exercícios 5 e 6)
def seed():
    from datetime import date
    seeds = [
        EventoCreate(nome="PythonBrasil 2025", data=date(2025, 10, 15), organizador="Ana Lima", local="São Paulo", descricao="Maior conf Python do BR"),
        EventoCreate(nome="FastAPI Meetup RJ", data=date(2025, 11, 3), organizador="Carlos Souza", local="Rio de Janeiro", descricao="Workshop prático de FastAPI"),
        EventoCreate(nome="DevOps Summit", data=date(2025, 12, 1), organizador="Beatriz Costa", local="Brasília", descricao="Tendências em DevOps e SRE"),
    ]
    for s in seeds:
        criar_evento(s)
