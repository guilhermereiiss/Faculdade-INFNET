from sqlmodel import SQLModel, Session, create_engine, select
from config import settings
from models.evento import Evento, EventoCreate, Inscricao
from models.usuario import Usuario

engine = create_engine(
    settings.database_url,
    # check_same_thread=False necessário apenas para SQLite
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {},
    echo=False,
)


def criar_tabelas():
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency injection de sessão para os endpoints."""
    with Session(engine) as session:
        yield session


# ── Operações de Evento ──────────────────────────────────────────────────────

def listar_eventos(session: Session) -> list[Evento]:
    return session.exec(select(Evento)).all()


def obter_evento(session: Session, evento_id: int) -> Evento | None:
    return session.get(Evento, evento_id)


def criar_evento(session: Session, dados: EventoCreate, owner_username: str) -> Evento:
    import uuid
    from itertools import count
    evento = Evento(
        **dados.model_dump(),
        organizador_id=f"ORG-{uuid.uuid4().hex[:8].upper()}",
        token_auditoria=str(uuid.uuid4()),
        owner_username=owner_username,
    )
    session.add(evento)
    session.commit()
    session.refresh(evento)
    return evento


def atualizar_evento(session: Session, evento_id: int, dados: EventoCreate) -> Evento | None:
    evento = session.get(Evento, evento_id)
    if not evento:
        return None
    for campo, valor in dados.model_dump().items():
        setattr(evento, campo, valor)
    session.add(evento)
    session.commit()
    session.refresh(evento)
    return evento


def deletar_evento(session: Session, evento_id: int) -> bool:
    evento = session.get(Evento, evento_id)
    if not evento:
        return False
    session.delete(evento)
    session.commit()
    return True


# ── Busca com query parametrizada (Ex 1) ─────────────────────────────────────

def buscar_eventos_por_nome(session: Session, termo: str) -> list[Evento]:
    """
    Exercício 1 — query parametrizada via SQLModel/SQLAlchemy.
    O SQLModel usa parâmetros de bind internamente (? no SQLite, $1 no Postgres),
    jamais concatenação de string. O valor de `termo` nunca é interpolado na SQL.
    """
    statement = select(Evento).where(Evento.nome.contains(termo))
    return session.exec(statement).all()


# ── Operações de Inscrição ───────────────────────────────────────────────────

def listar_inscricoes(session: Session) -> list[Inscricao]:
    return session.exec(select(Inscricao)).all()


def obter_inscricao(session: Session, inscricao_id: int) -> Inscricao | None:
    return session.get(Inscricao, inscricao_id)


def criar_inscricao(session: Session, evento_id: int, owner_username: str) -> Inscricao:
    inscricao = Inscricao(evento_id=evento_id, owner_username=owner_username)
    session.add(inscricao)
    session.commit()
    session.refresh(inscricao)
    return inscricao


# ── Operações de Usuário ─────────────────────────────────────────────────────

def obter_usuario(session: Session, username: str) -> Usuario | None:
    return session.get(Usuario, username)


def criar_usuario(session: Session, usuario: Usuario) -> Usuario:
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


# ── Comentários (Ex 5 — XSS stored) ─────────────────────────────────────────

# Comentários são armazenados como texto simples; o escape acontece no Jinja2
_comentarios: dict[int, list[str]] = {}  # evento_id → lista de comentários


def listar_comentarios(evento_id: int) -> list[str]:
    return _comentarios.get(evento_id, [])


def adicionar_comentario(evento_id: int, comentario: str):
    _comentarios.setdefault(evento_id, []).append(comentario)


# ── Seeds ────────────────────────────────────────────────────────────────────

def seed(session: Session):
    from datetime import date
    from auth.security import hash_password

    # Só faz seed se o banco estiver vazio
    if session.exec(select(Usuario)).first():
        return

    usuarios = [
        Usuario(username="gui",   hashed_password=hash_password("senha123"), papel="organizador"),
        Usuario(username="admin", hashed_password=hash_password("admin123"), papel="admin", mfa_habilitado=True),
        Usuario(username="joao",  hashed_password=hash_password("joao123"),  papel="participante"),
    ]
    for u in usuarios:
        session.add(u)

    eventos_seed = [
        Evento(nome="PythonBrasil 2025", data=date(2025, 10, 15), organizador="Gui Reis",
               local="São Paulo",      descricao="Maior conf Python do BR",
               organizador_id="ORG-0001", token_auditoria="tok-0001", owner_username="gui"),
        Evento(nome="FastAPI Meetup RJ",  data=date(2025, 11, 3),  organizador="Carlos Souza",
               local="Rio de Janeiro", descricao="Workshop prático de FastAPI",
               organizador_id="ORG-0002", token_auditoria="tok-0002", owner_username="gui"),
        Evento(nome="DevOps Summit",      data=date(2025, 12, 1),  organizador="Bea Costa",
               local="Brasília",       descricao="Tendências em DevOps e SRE",
               organizador_id="ORG-0003", token_auditoria="tok-0003", owner_username="admin"),
    ]
    for e in eventos_seed:
        session.add(e)

    session.commit()
