import uuid
from models.evento import EventoCreate, EventoInterno
from models.usuario import UsuarioDB

# Banco de eventos em memória 
_eventos: dict[int, EventoInterno] = {}
_next_id = 1


def listar_eventos() -> list[EventoInterno]:
    return list(_eventos.values())


def obter_evento(evento_id: int) -> EventoInterno | None:
    return _eventos.get(evento_id)


def criar_evento(dados: EventoCreate, owner_username: str) -> EventoInterno:
    global _next_id
    evento = EventoInterno(
        **dados.model_dump(),
        id=_next_id,
        organizador_id=f"ORG-{_next_id:04d}",
        token_auditoria=str(uuid.uuid4()),
        owner_username=owner_username,
    )
    _eventos[_next_id] = evento
    _next_id += 1
    return evento


def atualizar_evento(evento_id: int, dados: EventoCreate) -> EventoInterno | None:
    if evento_id not in _eventos:
        return None
    atual = _eventos[evento_id]
    atualizado = EventoInterno(
        **dados.model_dump(),
        id=atual.id,
        organizador_id=atual.organizador_id,
        token_auditoria=atual.token_auditoria,
        owner_username=atual.owner_username,
    )
    _eventos[evento_id] = atualizado
    return atualizado


def deletar_evento(evento_id: int) -> bool:
    if evento_id in _eventos:
        del _eventos[evento_id]
        return True
    return False


# Banco de usuários em memória
_usuarios: dict[str, UsuarioDB] = {}


def obter_usuario(username: str) -> UsuarioDB | None:
    return _usuarios.get(username)


def criar_usuario(usuario: UsuarioDB) -> UsuarioDB:
    _usuarios[usuario.username] = usuario
    return usuario


# Seeds
def seed():
    from datetime import date
    from auth.security import hash_password

    # Usuários seed
    usuarios_seed = [
        UsuarioDB(username="gui",   hashed_password=hash_password("senha123"), papel="organizador"),
        UsuarioDB(username="admin", hashed_password=hash_password("admin123"), papel="admin", mfa_habilitado=True),
        UsuarioDB(username="joao",  hashed_password=hash_password("joao123"),  papel="participante"),
    ]
    for u in usuarios_seed:
        _usuarios[u.username] = u

    # Eventos seed
    seeds = [
        (EventoCreate(nome="PythonBrasil 2025", data=date(2025, 10, 15), organizador="Gui Reis",     local="São Paulo",   descricao="Maior conf Python do BR"), "gui"),
        (EventoCreate(nome="FastAPI Meetup RJ",  data=date(2025, 11, 3),  organizador="Carlos Souza", local="Rio de Janeiro", descricao="Workshop prático de FastAPI"), "gui"),
        (EventoCreate(nome="DevOps Summit",      data=date(2025, 12, 1),  organizador="Bea Costa",    local="Brasília",    descricao="Tendências em DevOps e SRE"), "admin"),
    ]
    for dados, owner in seeds:
        criar_evento(dados, owner)
